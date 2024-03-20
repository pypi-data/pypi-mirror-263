# SPDX-FileCopyrightText: 2024-present dh031200 <imbird0312@gmail.com>
#
# SPDX-License-Identifier: MIT

import numpy as np
import torch
import torchvision


def wh2xy(x):
    y = x.clone()
    y[..., 0] = x[..., 0] - x[..., 2] / 2  # top left x
    y[..., 1] = x[..., 1] - x[..., 3] / 2  # top left y
    y[..., 2] = x[..., 0] + x[..., 2] / 2  # bottom right x
    y[..., 3] = x[..., 1] + x[..., 3] / 2  # bottom right y
    return y


def score_thresh(detections, thresh):
    nc = detections.shape[1] - 4  # number of classes
    xc = detections[:, 4 : 4 + nc].amax(1) > thresh  # candidates

    x = detections[0].transpose(0, -1)[xc[0]]  # confidence

    # Detections matrix nx6 (box, conf, cls)
    box, cls = x.split((4, nc), 1)

    # (center_x, center_y, width, height) to (x1, y1, x2, y2)
    box = wh2xy(box)
    if nc > 1:
        i, j = (cls > thresh).nonzero(as_tuple=False).T
        x = torch.cat((box[i], x[i, 4 + j, None], j[:, None].float()), 1)
    else:  # best class only
        conf, j = cls.max(1, keepdim=True)
        x = torch.cat((box, conf, j.float()), 1)[conf.view(-1) > thresh]

    return x


def soft_nms(detections, method="gaussian", iou_thr=0.3, sigma=0.5, score_thr=0.001):
    """Pure python implementation of soft NMS as described in the paper
    `Improving Object Detection With One Line of Code`_.

    Args:
        detections (numpy.array): Detection results with shape `(num, 5)`,
            data in second dimension are [x1, y1, x2, y2, score] respectively.
        method (str): Rescore method. Only can be `linear`, `gaussian`
            or 'greedy'.
        iou_thr (float): IOU threshold. Only work when method is `linear`
            or 'greedy'.
        sigma (float): Gaussian function parameter. Only work when method
            is `gaussian`.
        score_thr (float): Boxes that score less than score_thr.

    Returns:
        numpy.array: Retained boxes.

    . _`Improving Object Detection With One Line of Code`:
        https://arxiv.org/abs/1704.04503
    """
    if method not in ("linear", "gaussian", "greedy"):
        msg = "method must be linear, gaussian or greedy"
        raise ValueError(msg)

    dets = score_thresh(detections, score_thr)
    if not dets.shape[0]:
        return dets.numpy()

    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]

    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    # x1, y1, x2, y2, score, class, area
    dets = np.concatenate((dets, areas[:, None]), axis=1)

    retained_box = []
    while dets.size > 0:
        max_idx = np.argmax(dets[:, 4], axis=0)
        dets[[0, max_idx], :] = dets[[max_idx, 0], :]
        retained_box.append(dets[0, :-1])

        xx1 = np.maximum(dets[0, 0], dets[1:, 0])
        yy1 = np.maximum(dets[0, 1], dets[1:, 1])
        xx2 = np.minimum(dets[0, 2], dets[1:, 2])
        yy2 = np.minimum(dets[0, 3], dets[1:, 3])

        w = np.maximum(xx2 - xx1 + 1, 0.0)
        h = np.maximum(yy2 - yy1 + 1, 0.0)
        inter = w * h
        iou = inter / (dets[0, 6] + dets[1:, 6] - inter)

        if method == "linear":
            weight = np.ones_like(iou)
            weight[iou > iou_thr] -= iou[iou > iou_thr]
        elif method == "gaussian":
            weight = np.exp(-(iou * iou) / sigma)
        else:  # traditional nms
            weight = np.ones_like(iou)
            weight[iou > iou_thr] = 0

        dets[1:, 4] *= weight
        retained_idx = np.where(dets[1:, 4] >= score_thr)[0]
        dets = dets[retained_idx + 1, :]
    return np.vstack(retained_box)


def non_maximum_suppression(detections, conf_threshold=0.001, iou_threshold=0.3):
    nc = detections.shape[1] - 4  # number of classes
    xc = detections[:, 4 : 4 + nc].amax(1) > conf_threshold  # candidates

    # Settings
    max_wh = 7680  # (pixels) maximum box width and height
    max_det = 300  # the maximum number of boxes to keep after NMS
    max_nms = 30000  # maximum number of boxes into torchvision.ops.nms()

    outputs = torch.zeros((0, 6), device=detections.device)
    x = detections[0].transpose(0, -1)[xc[0]]  # confidence
    # If none remain process next image
    if not x.shape[0]:
        return outputs.numpy()

    # Detections matrix nx6 (box, conf, cls)
    box, cls = x.split((4, nc), 1)
    # (center_x, center_y, width, height) to (x1, y1, x2, y2)
    box = wh2xy(box)
    if nc > 1:
        i, j = (cls > conf_threshold).nonzero(as_tuple=False).T
        x = torch.cat((box[i], x[i, 4 + j, None], j[:, None].float()), 1)
    else:  # best class only
        conf, j = cls.max(1, keepdim=True)
        x = torch.cat((box, conf, j.float()), 1)[conf.view(-1) > conf_threshold]
    # Check shape
    if not x.shape[0]:  # no boxes
        return outputs.numpy()
    # sort by confidence and remove excess boxes
    x = x[x[:, 4].argsort(descending=True)[:max_nms]]

    # Batched NMS
    c = x[:, 5:6] * max_wh  # classes
    boxes, scores = x[:, :4] + c, x[:, 4]  # boxes (offset by class), scores

    return x[torchvision.ops.nms(boxes, scores, iou_threshold)[:max_det]].numpy()


__all__ = (
    "soft_nms",
    "non_maximum_suppression",
)
