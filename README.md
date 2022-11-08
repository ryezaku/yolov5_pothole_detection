# Mohammad Haziq - Pothole Detection Yolov5n & Yolov5m


- You may change to use whether yolov5n or yolov5m in the jupyter notebook file:
```
model =  torch.hub.load(r'yolov5', 'custom', path = r'runs\train\yolov5n\weights\best.pt', force_reload=True,source='local')
```

- You may also change the path of image here 
```
image = cv2.imread(r'C:\Users\user\Documents\yolov5\Dataset\train\G0010119.jpg')
```
