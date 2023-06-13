import cv2
import numpy as np
import math
from cv2 import dnn_superres

img = cv2.imread("filename.jpg")

sr = dnn_superres.DnnSuperResImpl_create()
path = 'LapSRN_x2.pb'
sr.readModel(path)
sr.setModel('lapsrn', 2)

def splitter():
    # Get the height and width of the image
    height, width = img.shape[:2]

    # Split the image into 4 equal parts
    half_height = height // 2
    half_width = width // 2

    top_left = img[:half_height, :half_width]
    top_right = img[:half_height, half_width:]
    bottom_left = img[half_height:, :half_width]
    bottom_right = img[half_height:, half_width:]

    # Save the resulting images to disk
    cv2.imwrite("top_left.jpg", top_left)
    cv2.imwrite("top_right.jpg", top_right)
    cv2.imwrite("bottom_left.jpg", bottom_left)
    cv2.imwrite("bottom_right.jpg", bottom_right)

def merger():
    top_left = cv2.imread("top_left.jpg")
    top_right = cv2.imread("top_right.jpg")
    bottom_left = cv2.imread("bottom_left.jpg")
    bottom_right = cv2.imread("bottom_right.jpg")

    # Resize the images to have dimensions that are evenly divisible by 2
    height, width = top_left.shape[:2]
    height -= height % 2
    width -= width % 2

    top_left = cv2.resize(top_left, (width, height))
    top_right = cv2.resize(top_right, (width, height))
    bottom_left = cv2.resize(bottom_left, (width, height))
    bottom_right = cv2.resize(bottom_right, (width, height))

    # Create a blank image with the same dimensions
    merged = np.zeros((height * 2, width * 2, 3), dtype=np.uint8)

    # Insert the images into the merged image
    merged[:height, :width] = top_left
    merged[:height, width:width * 2] = top_right
    merged[height:height * 2, :width] = bottom_left
    merged[height:height * 2, width:width * 2] = bottom_right

    # Save the merged image to disk
    cv2.imwrite("merged_image.jpg", merged)

def output(str):
    print("Final result: ", str)

def distance(original, new):
    return math.dist(original, new)

def cornerRect(img, bbox, l=10, t=2, rt=1, colorR=(0, 0, 255), colorC=(0, 255, 0)):
    x, y, w, h = bbox
    x1, y1 = x + w, y + h

    if rt != 0:
        cv2.rectangle(img, bbox, colorR, rt)

    # Top Left  x,y
    cv2.line(img, (x, y), (x + l, y), colorC, t)
    cv2.line(img, (x, y), (x, y + l), colorC, t)

    # Top Right  x1,y
    cv2.line(img, (x1, y), (x1 - l, y), colorC, t)
    cv2.line(img, (x1, y), (x1, y + l), colorC, t)

    # Bottom Left  x,y1
    cv2.line(img, (x, y1), (x + l, y1), colorC, t)
    cv2.line(img, (x, y1), (x, y1 - l), colorC, t)

    # Bottom Right  x1,y1
    cv2.line(img, (x1, y1), (x1 - l, y1), colorC, t)
    cv2.line(img, (x1, y1), (x1, y1 - l), colorC, t)

    return img