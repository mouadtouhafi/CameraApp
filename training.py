import os
import numpy as np
from PIL import Image
import cv2
import pickle

y_labels = []
x_train = []
current_id = 0
label_ids = {}

    # l'emplacement du programme actuel
    # print(BASE_DIR) nous donne C:\Users\poste\PycharmProjects\untitled2
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # après , on a utilisé la fonction .join pour accéder au répertoire suivant
    # print(image_dir) nous donne C:\Users\poste\PycharmProjects\untitled2\my_training_face
image_dir = os.path.join(BASE_DIR, "my_training_face")
face_cascade = cv2.CascadeClassifier("C://Users/poste/PycharmProjects/untitled2/data/haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
    #maintenant on va accéder à chaque fichier de notre répertoire
for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
            path = os.path.join(root, file)
                # mes images se trouvent dans le dossier "mouad", donc mouad sera le label de mes images
            label = os.path.basename(os.path.dirname(path))
            #print(path)
            #print(label)

            if not label in label_ids:
                label_ids[label]=current_id
                current_id += 1
            id_=label_ids[label]
            #print(label_ids)

            pil_image = Image.open(path).convert("L")   # in GrayScale
            image_array = np.array(pil_image, "uint8")  # on convertie les images en des tableaux numpy
            #print(image_array)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

            for(x,y,h,w) in faces:
                roi=image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

#print(y_labels)
#print(x_train)

with open("labels.pickle",'wb') as f:
    pickle.dump(label_ids,f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")