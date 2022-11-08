import cv2 
from paddleocr import PaddleOCR
import torch
import numpy as np
import os
string = []
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
plate_number_model =  torch.hub.load(r'C:\Users\User\Documents\jpj-awas-imaging-app-cyber\jpj-awas-imaging-trafficlight-number-plate-detector\app\module_external\yolov5', 'custom', path = r'C:\Users\User\Documents\jpj-awas-imaging-app-cyber\jpj-awas-imaging-trafficlight-number-plate-detector\app\resources\yolo_weight\lp_22Mar_best_e68_s6.pt', force_reload=True,source='local')
model_path = r'C:\Users\User\Documents\jpj-awas-imaging-app-cyber\jpj-awas-imaging-trafficlight-number-plate-detector\app\resources\yolo_weight\lp_22Mar_best_e68_s6.pt'
# plate_number_model.load_state_dict(torch.load(model_path, map_location='cpu'))
path = os.path.dirname(os.path.abspath(__file__))
Conf_threshold = 0.4
NMS_threshold = 0.4
image = cv2.imread(r'C:\Users\User\Desktop\cut corner\3.jpg')
model.conf = 0.31
model.iou = 0.6
results = model(image) 
image4 = cv2.resize(image, (int(image.shape[1]/3),int(image.shape[0]/3)))
cv2.imshow('image', image4)
cv2.waitKey(0)
df_results = results.pandas().xyxy[0]
for index,row in df_results.iterrows():
    print(row['name'])
    image_cropped = image[int(row['ymin']):int(row['ymax']),int(row['xmin']):int(row['xmax'])]
    print(image_cropped.shape)
    rat = image_cropped.shape[0]/image_cropped.shape[1]
    
    start = (int(row['xmin']), int(row['ymin']))
    end = (int(row['xmax']), int(row['ymax']))
    image2 = cv2.rectangle(image,start ,end,(0,255,0),3)
    

image2 = cv2.resize(image2, (int(image2.shape[1]/3),int(image2.shape[0]/3)))
cv2.imshow('image', image2)
cv2.waitKey(0)







    



