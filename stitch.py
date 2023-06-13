import cv2
import glob
import numpy as np
import matplotlib.pyplot as plt
import math

def main():
    '''
    mainFolder = 'images'
    myFolders = os.listdir(mainFolder)
    print(myFolders)
    #for folder in :
    folder = myFolders[1]
    path = mainFolder + '/' + myFolders[1]
    print(path)
    myList = os.listdir((path))
    print(f'Total images: {len(myList)}')

    images = []
    for imgN in myList:
        curImg = cv2.imread(f'{path}/{imgN}')
        #curImg = cv2.resize(curImg, (0, 0), None, 0.2, 0.2)
        images.append(curImg)

    print("Length of stitching images folder:", len(images))
    cv2.imshow("Frame", images[0])


    stitcher = cv2.Stitcher_create()
    (status, result) = stitcher.stitch(images)

    if(status == cv2.STITCHER_OK):
        print("Stitching complete")
        cv2.imshow(folder, result)
        cv2.waitKey(0)
    else:
        print("Stitching unsuccessful")
    '''

    image_paths = glob.glob('images/2/*')
    image_paths.sort()

    images = []
    for filename in image_paths:
        img = cv2.imread(filename)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        images.append(img)

    num_images = len(images)

    #Displaying images:
    plt.figure(figsize=[30,10])
    num_cols = 3
    num_rows = math.ceil(num_images/num_cols)
    for i in range(0,num_images):
        plt.subplot(num_rows, num_cols, i+1)
        plt.axis('off')
        plt.imshow(images[i])

    #stitching images
    stitcher = cv2.Stitcher_create()
    status, result = stitcher.stitch(images)

    if status == 0:
        plt.figure(figsize=[30,10])
        plt.imshow(result)
        #cv2.imwrite("output.png", result)
        #cv2.imshow("Stitched image", result)
        #cv2.waitKey(0)


if __name__ == '__main__':
    main()