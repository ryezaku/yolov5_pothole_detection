Pothole Detection Yolov5n & Yolov5m


- You may change to use whether yolov5n or yolov5m in the jupyter notebook file:
```
model =  torch.hub.load(r'yolov5', 'custom', path = r'runs\train\yolov5n\weights\best.pt', force_reload=True,source='local')
```

- You may also change the path of image here 
```
image = cv2.imread(r'C:\Users\user\Documents\yolov5\Dataset\train\G0010119.jpg')
```
- The latency of the model is shown in table below in CPU:

| Model  | Latency(ms) |
| ------ | ----------- |
| yolov5m.pt  | 350  |
| yolov5m.onnx  | 250  |
| yolov5m.pt  | 80  |
