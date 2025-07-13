import cv2
import pickle

face_cascade = cv2.CascadeClassifier("C://Users/poste/PycharmProjects/untitled2/data/haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name":1}
with open("labels.pickle",'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

def change_resolution(width, height):
    cap.set(3, width)
    cap.set(4, height)

change_resolution(320, 240)

while True:
    ret, frame = cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        id_,conf = recognizer.predict(roi_gray)
        if conf >= 45:
            print(id_)
            print(labels[id_])
        else:
            print("strainger")

