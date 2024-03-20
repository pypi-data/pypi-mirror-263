# SPDX-FileCopyrightText: 2024-present dh031200 <imbird0312@gmail.com>
#
# SPDX-License-Identifier: MIT

import cv2
import numpy as np
from supervision import Detections

coco_class_names = {
    0: "person",
    1: "bicycle",
    2: "car",
    3: "motorcycle",
    4: "airplane",
    5: "bus",
    6: "train",
    7: "truck",
    8: "boat",
    9: "traffic light",
    10: "fire hydrant",
    11: "stop sign",
    12: "parking meter",
    13: "bench",
    14: "bird",
    15: "cat",
    16: "dog",
    17: "horse",
    18: "sheep",
    19: "cow",
    20: "elephant",
    21: "bear",
    22: "zebra",
    23: "giraffe",
    24: "backpack",
    25: "umbrella",
    26: "handbag",
    27: "tie",
    28: "suitcase",
    29: "frisbee",
    30: "skis",
    31: "snowboard",
    32: "sports ball",
    33: "kite",
    34: "baseball bat",
    35: "baseball glove",
    36: "skateboard",
    37: "surfboard",
    38: "tennis racket",
    39: "bottle",
    40: "wine glass",
    41: "cup",
    42: "fork",
    43: "knife",
    44: "spoon",
    45: "bowl",
    46: "banana",
    47: "apple",
    48: "sandwich",
    49: "orange",
    50: "broccoli",
    51: "carrot",
    52: "hot dog",
    53: "pizza",
    54: "donut",
    55: "cake",
    56: "chair",
    57: "couch",
    58: "potted plant",
    59: "bed",
    60: "dining table",
    61: "toilet",
    62: "tv",
    63: "laptop",
    64: "mouse",
    65: "remote",
    66: "keyboard",
    67: "cell phone",
    68: "microwave",
    69: "oven",
    70: "toaster",
    71: "sink",
    72: "refrigerator",
    73: "book",
    74: "clock",
    75: "vase",
    76: "scissors",
    77: "teddy bear",
    78: "hair drier",
    79: "toothbrush",
}

TRACK_SHAPE = 7


def make_labels(detections, class_names=None):
    class_names = coco_class_names if class_names is None else class_names

    if detections.tracker_id is None:
        labels = [
            f"{class_names[class_id]} {conf}%" for class_id, conf in zip(detections.class_id, detections.confidence)
        ]
    else:
        labels = [
            f"{tracker_id} {class_names[class_id]} {conf}%"
            for tracker_id, class_id, conf in zip(detections.tracker_id, detections.class_id, detections.confidence)
        ]
    return labels


def to_supervision_detections(detections, *, class_agnostic=False):
    """
    :param detections: np.array([x1, y1, x2, y2, conf, class, track_id])
    :return:Detections
    """
    if not isinstance(detections, np.ndarray):
        detections.numpy()

    detections[:, 4] *= 100
    detections = detections.astype(int)

    return Detections(
        xyxy=detections[:, :4],
        confidence=detections[:, 4],
        class_id=detections[:, 5] if all([not class_agnostic, detections.shape[1]]) else detections[:, 6],
        tracker_id=detections[:, 6] if detections.shape[1] == TRACK_SHAPE else None,
    )


def resize(image, input_size):
    # Resize and pad image while meeting stride-multiple constraints
    shape = image.shape[:2]  # current shape [height, width]

    # Scale ratio (new / old)
    r = min(input_size / shape[0], input_size / shape[1], 1.0)

    # Compute padding
    pad = int(round(shape[1] * r)), int(round(shape[0] * r))
    w = (input_size - pad[0]) / 2
    h = (input_size - pad[1]) / 2

    if shape[::-1] != pad:  # resize
        image = cv2.resize(image, dsize=pad, interpolation=cv2.INTER_LINEAR)
    top, bottom = int(round(h - 0.1)), int(round(h + 0.1))
    left, right = int(round(w - 0.1)), int(round(w + 0.1))
    image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT)  # add border
    return image, (r, r), (w, h)


def scale(coords, shape1, shape2, ratio_pad=None):
    if ratio_pad is None:  # calculate from img0_shape
        gain = min(shape1[0] / shape2[0], shape1[1] / shape2[1])  # gain  = old / new
        pad = (shape1[1] - shape2[1] * gain) / 2, (shape1[0] - shape2[0] * gain) / 2  # wh padding
    else:
        gain = min(ratio_pad[0])
        pad = ratio_pad[1]

    coords[:, [0, 2]] -= pad[0]  # x padding
    coords[:, [1, 3]] -= pad[1]  # y padding
    coords[:, :4] /= gain

    coords[:, 0].clip(0, shape2[1])  # x1
    coords[:, 1].clip(0, shape2[0])  # y1
    coords[:, 2].clip(0, shape2[1])  # x2
    coords[:, 3].clip(0, shape2[0])  # y2
    return coords
