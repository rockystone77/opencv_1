import numpy as np
import cv2 as cv

people = ['Madonna', 'Elton John', 'Jerry Seinfield', 'Mindy Kaling', 'Ben Afflek']

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# features = np.load('features.npy')
# leabels = np.load('labels.npy')

faces_recognizer = cv.face.LBPHFaceRecognizer_create()
faces_recognizer.read('face_trained.yml')

img = cv.imread(r'/home/peterjung/Documents/opencv-workspace/Faces/val/ben_afflek/5.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Person', gray)

#detect the face in iumage
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    label, confidence = faces_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2 )

cv.imshow('Detected Face', img)
cv.waitKey(0)