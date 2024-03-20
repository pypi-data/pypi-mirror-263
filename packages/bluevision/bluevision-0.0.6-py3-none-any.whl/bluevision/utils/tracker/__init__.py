# SPDX-FileCopyrightText: 2024-present dh031200 <imbird0312@gmail.com>
#
# SPDX-License-Identifier: MIT

from .bytetrack import BYTETracker


class Tracker:
    def __init__(self, method=None):
        if method == "bytetrack":
            tracker = BYTETracker()
        else:
            tracker = BYTETracker()
        self.tracker = tracker

    def __call__(self, detections):
        return self.tracker.update(detections)

    def get_origin(self):
        return [i.init_coords for i in self.tracker.tracked_stracks]


__all__ = ("Tracker",)
