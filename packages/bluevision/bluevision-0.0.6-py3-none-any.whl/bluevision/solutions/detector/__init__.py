# SPDX-FileCopyrightText: 2024-present dh031200 <imbird0312@gmail.com>
#
# SPDX-License-Identifier: MIT
from loguru import logger

from bluevision.utils.nms import non_maximum_suppression

# Import simplify
from . import models


class Detector:
    def __init__(self, model, weights=None, nms=None):
        self.model = model
        self.model.set_nms(non_maximum_suppression if nms is None else nms)

        if weights is not None:
            self.load(weights)

        logger.info(f"Using {model.device}")
        logger.info(f"Model: {model.__class__.__name__}")
        logger.info(f"Weights: {weights}")
        logger.info(f"NMS: {model.nms.__name__}")

    def load(self, weights_path):
        self.model.load(weights_path)

    def __call__(self, image):
        return self.model(image)


__all__ = ("models", "Detector")
