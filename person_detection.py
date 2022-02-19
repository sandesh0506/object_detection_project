import cv2
import sys


class PersonDetection:

    def person_detection_function(self, file_name):
        # fetch image original folder path
        imagePath = file_name
        cascPath = 'haarcascade_files/haarcascade_frontalface_default.xml';

        faceCascase = cv2.CascadeClassifier(cascPath)
        # read the image in imagePath
        image = cv2.imread(imagePath)
        # convert the image into gray colored image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascase.detectMultiScale(
            gray,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize=(30,30),
            # flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        # print number of faces found in console
        print("Found {0} faces!".format(len(faces)))

        # draw rectangle in red around the faces
        for(x,y, w, h) in faces:
            cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)

        # show the image
        cv2.imshow("Faces Found", image)
        cv2.waitKey(0)


