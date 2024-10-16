# SmartVision: A Computer Vision based solution to find items in indoor environments. 

This repository contains the codes for a product prototype aimed at helping people locate misplaced items in a confined and indoor environments. It consists of a wall mounted camera, object detection software and a voice assistant enable application for easy accessibility.

---
## Contents:
1. Description
2. Installation requirements
3. Intuition
4. Contact

---
### 1.Description:
The product prototype consists of a Pan-Tilt-Zoom camera with Raspberry Pi to help people locate misplaced items indoors. It is trained on Yolo V5 object detection model (84% accuracy) to detect objects in confined environments under varying lighting and occlusion conditions. The model is convert from *.pt* format to *.onnx* format. 

### 2. Requirements and installation:

**Requirements**
```
Python 3.8
Main libraries used: OpenCV, Numpy
```

### 3. Intuition:
In this project, an image is captured using the camera first. SuperResolution is applied to increase the image dimensions by 4 times, so that the visibility increases. This image is sliced into 6 parts (3 cols and 2 rows) and fed to the object detection model. The model has two lists: small objects and large objects. Once the object is located, it gives a message saying where the object is. 
Example: `The bottle is on top of the table`

### 4. Contact:
For more information about the project, please feel free to reach out at: das20ucse101@mahindrauniversity.edu.in

---




