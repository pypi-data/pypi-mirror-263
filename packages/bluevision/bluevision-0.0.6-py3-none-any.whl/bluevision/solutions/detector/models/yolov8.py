# SPDX-FileCopyrightText: 2024-present dh031200 <imbird0312@gmail.com>
#
# SPDX-License-Identifier: MIT

import math

import numpy as np
import torch
from safetensors.torch import load, save_file

from bluevision.utils import resize, scale


def make_anchors(x, strides, offset=0.5):
    """
    Generate anchors from features
    """
    if x is None:
        msg = "Expected 'x' value."
        raise ValueError(msg)
    anchor_points, stride_tensor = [], []

    _, _, h, w = x[0].shape
    sx = torch.arange(end=w, dtype=x[0].dtype, device=x[0].device) + offset  # shift x
    sy = torch.arange(end=h, dtype=x[0].dtype, device=x[0].device) + offset  # shift y
    sy, sx = torch.meshgrid(sy, sx, indexing="ij")
    anchor_points.append(torch.stack((sx, sy), -1).view(-1, 2))
    stride_tensor.append(torch.full((h * w, 1), strides[0], dtype=x[0].dtype, device=x[0].device))

    _, _, h, w = x[1].shape
    sx = torch.arange(end=w, dtype=x[1].dtype, device=x[1].device) + offset  # shift x
    sy = torch.arange(end=h, dtype=x[1].dtype, device=x[1].device) + offset  # shift y
    sy, sx = torch.meshgrid(sy, sx, indexing="ij")
    anchor_points.append(torch.stack((sx, sy), -1).view(-1, 2))
    stride_tensor.append(torch.full((h * w, 1), strides[1], dtype=x[1].dtype, device=x[1].device))

    _, _, h, w = x[2].shape
    sx = torch.arange(end=w, dtype=x[2].dtype, device=x[2].device) + offset  # shift x
    sy = torch.arange(end=h, dtype=x[2].dtype, device=x[2].device) + offset  # shift y
    sy, sx = torch.meshgrid(sy, sx, indexing="ij")
    anchor_points.append(torch.stack((sx, sy), -1).view(-1, 2))
    stride_tensor.append(torch.full((h * w, 1), strides[2], dtype=x[2].dtype, device=x[2].device))

    return torch.cat(anchor_points), torch.cat(stride_tensor)


def pad(k, p=None, d=1):
    if d > 1:
        k = d * (k - 1) + 1
    if p is None:
        p = k // 2
    return p


def fuse_conv(conv, norm):
    fused_conv = (
        torch.nn.Conv2d(
            conv.in_channels,
            conv.out_channels,
            kernel_size=conv.kernel_size,
            stride=conv.stride,
            padding=conv.padding,
            groups=conv.groups,
            bias=True,
        )
        .requires_grad_(False)
        .to(conv.weight.device)
    )

    w_conv = conv.weight.clone().view(conv.out_channels, -1)
    w_norm = torch.diag(norm.weight.div(torch.sqrt(norm.eps + norm.running_var)))
    fused_conv.weight.copy_(torch.mm(w_norm, w_conv).view(fused_conv.weight.size()))

    b_conv = torch.zeros(conv.weight.size(0), device=conv.weight.device) if conv.bias is None else conv.bias
    b_norm = norm.bias - norm.weight.mul(norm.running_mean).div(torch.sqrt(norm.running_var + norm.eps))
    fused_conv.bias.copy_(torch.mm(w_norm, b_conv.reshape(-1, 1)).reshape(-1) + b_norm)

    return fused_conv


class Conv(torch.nn.Module):
    def __init__(self, in_ch, out_ch, k=1, s=1, p=None, d=1, g=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_ch, out_ch, k, s, pad(k, p, d), d, g, False)
        self.norm = torch.nn.BatchNorm2d(out_ch, 0.001, 0.03)
        self.relu = torch.nn.SiLU(inplace=True)

    def forward(self, x):
        return self.relu(self.norm(self.conv(x)))

    def fuse_forward(self, x):
        return self.relu(self.conv(x))


class Residual(torch.nn.Module):
    def __init__(self, ch, *, add=True):
        super().__init__()
        self.add_m = add
        self.res_m = torch.nn.Sequential(Conv(ch, ch, 3), Conv(ch, ch, 3))

    def forward(self, x):
        return self.res_m(x) + x if self.add_m else self.res_m(x)


class CSP(torch.nn.Module):
    def __init__(self, in_ch, out_ch, n=1, *, add=True):
        super().__init__()
        self.conv1 = Conv(in_ch, out_ch // 2)
        self.conv2 = Conv(in_ch, out_ch // 2)
        self.conv3 = Conv((2 + n) * out_ch // 2, out_ch)
        self.res_m = torch.nn.ModuleList(Residual(out_ch // 2, add=add) for _ in range(n))

    def forward(self, x):
        y = [self.conv1(x), self.conv2(x)]
        y.extend(m(y[-1]) for m in self.res_m)
        return self.conv3(torch.cat(y, dim=1))


class SPP(torch.nn.Module):
    def __init__(self, in_ch, out_ch, k=5):
        super().__init__()
        self.conv1 = Conv(in_ch, in_ch // 2)
        self.conv2 = Conv(in_ch * 2, out_ch)
        self.res_m = torch.nn.MaxPool2d(k, 1, k // 2)

    def forward(self, x):
        x = self.conv1(x)
        y1 = self.res_m(x)
        y2 = self.res_m(y1)
        return self.conv2(torch.cat([x, y1, y2, self.res_m(y2)], 1))


class DarkNet(torch.nn.Module):
    def __init__(self, width, depth):
        super().__init__()
        p1 = [Conv(width[0], width[1], 3, 2)]
        p2 = [Conv(width[1], width[2], 3, 2), CSP(width[2], width[2], depth[0])]
        p3 = [Conv(width[2], width[3], 3, 2), CSP(width[3], width[3], depth[1])]
        p4 = [Conv(width[3], width[4], 3, 2), CSP(width[4], width[4], depth[2])]
        p5 = [Conv(width[4], width[5], 3, 2), CSP(width[5], width[5], depth[0]), SPP(width[5], width[5])]

        self.p1 = torch.nn.Sequential(*p1)
        self.p2 = torch.nn.Sequential(*p2)
        self.p3 = torch.nn.Sequential(*p3)
        self.p4 = torch.nn.Sequential(*p4)
        self.p5 = torch.nn.Sequential(*p5)

    def forward(self, x):
        p1 = self.p1(x)
        p2 = self.p2(p1)
        p3 = self.p3(p2)
        p4 = self.p4(p3)
        p5 = self.p5(p4)
        return p3, p4, p5


class DarkFPN(torch.nn.Module):
    def __init__(self, width, depth):
        super().__init__()
        self.up = torch.nn.Upsample(None, 2)
        self.h1 = CSP(width[4] + width[5], width[4], depth[0], add=False)
        self.h2 = CSP(width[3] + width[4], width[3], depth[0], add=False)
        self.h3 = Conv(width[3], width[3], 3, 2)
        self.h4 = CSP(width[3] + width[4], width[4], depth[0], add=False)
        self.h5 = Conv(width[4], width[4], 3, 2)
        self.h6 = CSP(width[4] + width[5], width[5], depth[0], add=False)

    def forward(self, x):
        p3, p4, p5 = x[0], x[1], x[2]
        h1 = self.h1(torch.cat([self.up(p5), p4], 1))
        h2 = self.h2(torch.cat([self.up(h1), p3], 1))
        h4 = self.h4(torch.cat([self.h3(h2), h1], 1))
        h6 = self.h6(torch.cat([self.h5(h4), p5], 1))
        return h2, h4, h6


class DFL(torch.nn.Module):
    # Integral module of Distribution Focal Loss (DFL)
    # Generalized Focal Loss https://ieeexplore.ieee.org/document/9792391
    def __init__(self, ch=16):
        super().__init__()
        self.ch = ch
        self.conv = torch.nn.Conv2d(ch, 1, 1, bias=False).requires_grad_(False)
        x = torch.arange(ch, dtype=torch.float).view(1, ch, 1, 1)
        self.conv.weight.data[:] = torch.nn.Parameter(x)

    def forward(self, x):
        b, c, a = x.shape
        x = x.view(b, 4, self.ch, a).transpose(2, 1)
        return self.conv(x.softmax(1)).view(b, 4, a)


class Head(torch.nn.Module):
    anchors = torch.empty(0)
    strides = torch.empty(0)

    def __init__(self, nc=80, filters=()):
        super().__init__()
        self.ch = 16  # DFL channels
        self.nc = nc  # number of classes
        self.nl = len(filters)  # number of detection layers
        self.no = nc + self.ch * 4  # number of outputs per anchor
        self.stride = torch.zeros(self.nl)  # strides computed during build

        c1 = max(filters[0], self.nc)
        c2 = max((filters[0] // 4, self.ch * 4))

        self.dfl = DFL(self.ch)
        self.cls = torch.nn.ModuleList(
            torch.nn.Sequential(Conv(x, c1, 3), Conv(c1, c1, 3), torch.nn.Conv2d(c1, self.nc, 1)) for x in filters
        )
        self.box = torch.nn.ModuleList(
            torch.nn.Sequential(Conv(x, c2, 3), Conv(c2, c2, 3), torch.nn.Conv2d(c2, 4 * self.ch, 1)) for x in filters
        )

    def forward(self, x):
        x[0] = torch.cat((self.box[0](x[0]), self.cls[0](x[0])), 1)
        x[1] = torch.cat((self.box[1](x[1]), self.cls[1](x[1])), 1)
        x[2] = torch.cat((self.box[2](x[2]), self.cls[2](x[2])), 1)
        if self.training:
            return x

        self.anchors, self.strides = (x.transpose(0, 1) for x in make_anchors(x, self.stride, 0.5))

        x = torch.cat([i.view(x[0].shape[0], self.no, -1) for i in x], 2)
        box, cls = x.split((self.ch * 4, self.nc), 1)
        a, b = torch.split(self.dfl(box), 2, 1)
        a = self.anchors.unsqueeze(0) - a
        b = self.anchors.unsqueeze(0) + b
        box = torch.cat(((a + b) / 2, b - a), 1)
        return torch.cat((box * self.strides, cls.sigmoid()), 1)

    def initialize_biases(self):
        # Initialize biases
        # WARNING: requires stride availability
        m = self
        for a, b, s in zip(m.box, m.cls, m.stride):
            a[-1].bias.data[:] = 1.0  # box
            # cls (.01 objects, 80 classes, 640 img)
            b[-1].bias.data[: m.nc] = math.log(5 / m.nc / (640 / s) ** 2)


class YOLO(torch.nn.Module):
    def __init__(self, width, depth, num_classes):
        super().__init__()
        self.net = DarkNet(width, depth)
        self.fpn = DarkFPN(width, depth)

        img_dummy = torch.zeros(1, 3, 256, 256)
        self.head = Head(num_classes, (width[3], width[4], width[5]))
        self.head.stride = torch.tensor([256 / x.shape[-2] for x in self.forward(img_dummy)])
        self.stride = self.head.stride
        self.head.initialize_biases()

    def forward(self, x):
        x = self.net(x)
        x = self.fpn(x)
        return self.head(list(x))

    def fuse(self):
        for m in self.modules():
            if type(m) is Conv and hasattr(m, "norm"):
                m.conv = fuse_conv(m.conv, m.norm)
                m.forward = m.fuse_forward
                delattr(m, "norm")
        return self


def yolo_v8_n(num_classes: int = 80):
    depth = [1, 2, 2]
    width = [3, 16, 32, 64, 128, 256]
    return YOLO(width, depth, num_classes)


def yolo_v8_s(num_classes: int = 80):
    depth = [1, 2, 2]
    width = [3, 32, 64, 128, 256, 512]
    return YOLO(width, depth, num_classes)


def yolo_v8_m(num_classes: int = 80):
    depth = [2, 4, 4]
    width = [3, 48, 96, 192, 384, 576]
    return YOLO(width, depth, num_classes)


def yolo_v8_l(num_classes: int = 80):
    depth = [3, 6, 6]
    width = [3, 64, 128, 256, 512, 512]
    return YOLO(width, depth, num_classes)


def yolo_v8_x(num_classes: int = 80):
    depth = [3, 6, 6]
    width = [3, 80, 160, 320, 640, 640]
    return YOLO(width, depth, num_classes)


class Yolov8:
    def __init__(self, size="n", device=None):
        if size == "n":
            model = yolo_v8_n
        elif size == "s":
            model = yolo_v8_s
        elif size == "m":
            model = yolo_v8_m
        elif size == "l":
            model = yolo_v8_l
        elif size == "x":
            model = yolo_v8_x
        else:
            msg = "Invalid size parameter"
            raise ValueError(msg)

        if device is None:
            if torch.cuda.is_available():
                _device = torch.device("cuda")
            elif torch.backends.mps.is_available():
                _device = torch.device("mps")
            else:
                _device = torch.device("cpu")
        else:
            _device = torch.device(device)
        self.device = _device
        self.model = model()
        self.nms = None

    def set_nms(self, nms):
        self.nms = nms

    def load(self, weights_path):
        with open(weights_path, "rb") as f:
            state_dict = load(f.read())
        self.model.load_state_dict(state_dict)
        self.model.to(self.device)
        self.model.eval()
        if self.device != torch.device("cpu"):
            self.model.half()

        # Warm up
        warm_up_data = torch.rand(1, 3, 640, 640).to(self.device)
        self.model(warm_up_data if self.device == torch.device("cpu") else warm_up_data.half())

    def preprocess(self, image):
        shape = image.shape[:2]
        image, ratio, _pad = resize(image, 640)
        h, w = image.shape[:2]
        shapes = shape, ((h / shape[0], w / shape[1]), _pad)

        sample = image.transpose((2, 0, 1))[::-1]
        input_data = torch.from_numpy(np.ascontiguousarray(sample)) / 255
        input_data.unsqueeze_(0)
        input_data = input_data.to(self.device)
        return input_data.half() if self.device != torch.device("cpu") else input_data, shapes

    def inference(self, data):
        return self.model(data).cpu()

    def postprocess(self, detections, input_shape, original_shape):
        if self.nms is not None:
            detections = self.nms(detections)
        return scale(detections, input_shape, original_shape[0], original_shape[1])

    def save(self, weights_path="model.safetensors"):
        save_file(self.model.state_dict(), weights_path)

    @torch.no_grad()
    def __call__(self, image):
        input_data, shapes = self.preprocess(image)
        prediction = self.inference(input_data)
        outputs = self.postprocess(prediction, input_data.shape, shapes)
        return outputs

    def to(self, device):
        self.model.to(device)

    def eval(self):
        self.model.eval()

    def half(self):
        self.model.half()
