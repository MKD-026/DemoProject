import cv2
import numpy as np
import math


file = open("COCO/coco.txt","r")
classes = file.read().split('\n')
classes = ['bottle']
#===========================================================================

bottleModel = cv2.dnn.readNetFromONNX("models/FINALbest.onnx")
#=====================================================================
def midpoint(x1,y1,x2,y2):
    xm = (x1+x2)//2     
    ym = (y1+y2)//2
    return xm, ym

def distance(original, new):
    return math.dist(original, new)

def finderImage(search_id):
    img = cv2.imread("media/66.jpeg")

    # Read about blob later
    blob = cv2.dnn.blobFromImage(img, scalefactor=1 / 255, size=(640, 640), mean=[0, 0, 0], swapRB=True, crop=False)
    bottleModel.setInput(blob)
    detections = bottleModel.forward()[0]

    classes_ids = []
    confidences = []
    boxes = []
    rows = detections.shape[0]

    img_width, img_height = img.shape[1], img.shape[0]
    x_scale = img_width / 640
    y_scale = img_height / 640

    for i in range(rows):
        row = detections[i]
        confidence = row[4]
        if confidence > 0.4:
            classes_score = row[5:]
            ind = np.argmax(classes_score)
            if classes_score[ind] > 0.5:
                classes_ids.append(ind)
                confidences.append(confidence)
                cx, cy, w, h = row[:4]
                x1 = int((cx - w / 2) * x_scale)
                y1 = int((cy - h / 2) * y_scale)
                width = int(w * x_scale)
                height = int(h * y_scale)
                box = np.array([x1, y1, width, height])
                boxes.append(box)

    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.5)

    coordinates = []
    objects = []
    original = (-1, -1)
    for i in indices:
        x1, y1, w, h = boxes[i]
        xm, ym = midpoint(x1,y1, x1+w, y1+h)
        label = classes[classes_ids[i]]
        conf = confidences[i]
        print(label, xm, ym)

        #getting coordinates of search_id
        if label == classes[search_id]:
           original = (xm, ym)
           text = label + " {:.2f}".format(conf)
           cv2.putText(img, text, (x1, y1 - 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
           cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (255, 0, 0), 2)

        #cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (255, 0, 0), 2)
        if label != classes[search_id]:
            objects.append(label)
            coordinates.append((xm, ym))

    cv2.imshow("Result", img)
    cv2.waitKey(0)

if __name__ == '__main__':
    #default value
    search_id = 0

    #finderVideo(search_id)
    finderImage(search_id)

