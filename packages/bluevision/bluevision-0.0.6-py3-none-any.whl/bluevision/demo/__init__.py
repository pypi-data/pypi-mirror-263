# SPDX-FileCopyrightText: 2024-present dh031200 <imbird0312@gmail.com>
#
# SPDX-License-Identifier: MIT

import cv2
import supervision as sv

import bluevision as bv
from bluevision.utils import make_labels, to_supervision_detections


def video_demo(weights, video_path, model_size="s", save_path=None, *, track=True, show=True):
    box_annotator = sv.BoundingBoxAnnotator(thickness=2)
    label_annotator = sv.LabelAnnotator(text_scale=0.5, text_padding=2)
    tracker = bv.utils.tracker.Tracker(method="bytetrack")
    detector = bv.solutions.Detector(
        model=bv.solutions.detector.models.Yolov8(size=model_size), nms=bv.utils.nms.soft_nms, weights=weights
    )

    # Load sample video
    vid = cv2.VideoCapture(video_path)

    # Writer initialize
    if save_path is not None:
        writer = cv2.VideoWriter(
            save_path,
            cv2.VideoWriter_fourcc(*"mp4v"),
            int(vid.get(cv2.CAP_PROP_FPS)),
            (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))),
        )
    else:
        writer = None

    # Start
    while True:
        ret, original_image = vid.read()
        if not ret:
            break

        detections = detector(original_image)
        if track:
            tracker.update(detections)
            detections = tracker.get_tracks()

        if any([show, save_path]):
            sv_detections = to_supervision_detections(detections)
            annotated_frame = box_annotator.annotate(
                scene=original_image,
                detections=sv_detections,
            )
            annotated_frame = label_annotator.annotate(
                scene=annotated_frame, detections=sv_detections, labels=make_labels(sv_detections)
            )
        else:
            annotated_frame = original_image

        if show:
            cv2.imshow("annotated image", annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        if save_path is not None:
            writer.write(annotated_frame)
    if save_path:
        writer.release()
    cv2.destroyAllWindows()
