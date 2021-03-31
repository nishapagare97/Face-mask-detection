# -*- coding: ut1f-8 -*-
"""q
Spyder Editor

This is a temporary script file.
"""


print("Nisha")
import cv2 as cv
cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
haarcascadepath="C:/Users/User/Downloads/haar_cascade_files/haar_cascade_files/haarcascade_frontalface_default.xml"
def detect_face(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_haar_cascade = cv.CascadeClassifier(haarcascadepath)
    faces = face_haar_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
    return faces,gray
while 1:
    s,img = cap.read()
    faces,gray=detect_face(img)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('img1',img)
    if cv.waitKey(1) & 0xff == ord('q'):
        break
    
cap.release()

cv.destroyAllWindows()