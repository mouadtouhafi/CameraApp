import cv2
import numpy as np
import pickle

face_cascade = cv2.CascadeClassifier("C://Users/poste/PycharmProjects/untitled2/data/haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name":1}
with open("labels.pickle",'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
def make_1080p():
    cap.set(3,1920)
    cap.set(4,1080)

def make_720p():
    cap.set(3,1280)
    cap.set(4,720)

def make_480p():
    cap.set(3,640)
    cap.set(4,480)

def change_resolution(width, height):
    cap.set(3, width)
    cap.set(4, height)

change_resolution(320, 240)

while True:
    ret, frame = cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        #print (x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        img_item = "C://Users/poste/Music/my_image.png"
        cv2.imwrite(img_item, roi_gray)

        id_,conf = recognizer.predict(roi_gray)
        if conf >=45: # and conf <= 85:
            print(id_)
            print(labels[id_])

        color = (255, 0, 0)
        stroke = 2
        width = x + w
        height = y + h
        cv2.rectangle(frame, (x,y), (width,height), color, stroke)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()