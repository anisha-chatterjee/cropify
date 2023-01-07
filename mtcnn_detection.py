# https://github.com/ipazc/mtcnn

from mtcnn import MTCNN
import cv2
import json

detector = MTCNN()

# DOES NOT ACCOUNT FOR IMAGES THAT ARE TOO CROPPED TO THE FACE ALREADY
def detect(i, num):

    img = cv2.imread(i)

    detect = detector.detect_faces(img)

    # bounding box from face detector
    output = detect[0]['box']
    (x, y, w, h) = (output[0], output[1], output[2], output[3])
    
    # expand bounding box
    offset = int((w+h)/5)
    (nw, nh) = (w + offset, h + offset)
    (nx, ny) = (x-offset, y-offset)

    # draw bounding rectangle
    # cv2.rectangle(img, (nx, ny), (x+nw, y+nh), (255, 0, 0), 2)

    # crop & save image
    cropped = img[ny:(y+nh), nx:(x+nw)]
    cv2.imwrite('mtcnn-output/' + str(num) + '.png', cropped)

    print('success' + str(num))

# run test images
detect('test-images/1.jpg', 1)
detect('test-images/2.jpg', 2)
detect('test-images/3.jpg', 3)
detect('test-images/4.jpg', 4)
#detect('test-images/5.jpeg', 5)
detect('test-images/6.jpg', 6)
detect('test-images/7.jpeg', 7)