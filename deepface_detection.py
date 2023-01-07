# import libraries
from deepface import DeepFace
from deepface.commons import functions
import cv2

# different models
detectors = ["opencv", "ssd", "mtcnn", "dlib", "retinaface"]

def detect(i, num):

    #detect face
    face = functions.preprocess_face(i, detector_backend=detectors[4])[0]
    
    #create output
    cv2.imwrite('deepface-output/' + str(num) + '.jpg', face*225)

    print('success' + str(num))

#run test images
detect('test-images/1.jpg', 1)
#detect('test-images/2.jpg', 2)
#detect('test-images/3.jpg', 3)
#detect('test-images/4.jpg', 4)
#detect('test-images/5.jpeg', 5)
#detect('test-images/6.jpg', 6)
#detect('test-images/7.jpeg', 7)
