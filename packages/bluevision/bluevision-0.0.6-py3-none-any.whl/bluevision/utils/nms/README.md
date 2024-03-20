## Non Maximum Suppression

### Greedy NMS

non_maximum_suppression(detections, conf_threshold=0.001, iou_threshold=0.3)
> detections(torch.tensor): detection outputs
> 

### Soft NMS

soft_nms(detections, method="gaussian", iou_thr=0.3, sigma=0.5, score_thr=0.001)