#https://towardsdatascience.com/simple-face-detection-in-python-1fcda0ea648e

import cv2

#load cascade
face_cascade = cv2.CascadeClassifier('face_detector.xml')

def find_face(i, num):
    #import image
    img = cv2.imread(i)

    #detect face
    face = face_cascade.detectMultiScale(img, 1.1, 4)

    #draw rectangle
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    #create output
    cv2.imwrite('simple-output/' + str(num) + '.png', img)

    print('success' + str(num))

#run test images
find_face('test-images/1.jpg', 1)
find_face('test-images/2.jpg', 2)
find_face('test-images/3.jpg', 3)
#find_face('test-images/4.jpg', 4)
find_face('test-images/5.jpeg', 5)
find_face('test-images/6.jpg', 6)
find_face('test-images/7.jpeg', 7)