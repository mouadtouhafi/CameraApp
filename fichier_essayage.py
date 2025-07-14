# file1 = open('C://Users/poste/Desktop/FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM/test.txt', 'r')
# Lines = file1.readlines()
#
# count = 0
# Noms = []
# Prenoms = []
# for line in Lines:
#     for word in line.split():
#         if word.__contains__('-'):
#             Noms.append(word.strip('-'))
#         if word.__contains__('_'):
#             Prenoms.append(word.strip('_'))

# print(Noms)
# print(Prenoms)

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os

BASE_DIR = os.path.dirname(os.path.relpath(__file__))
image_dir = os.path.join(BASE_DIR, "my_training_face")


def listDir(dir):
    global names
    global dict
    names = []
    dict = {}
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        names.append(fileName)
    i = 0
    while i < len(names):
        dict[i] = (names[i])
        i = i + 1
    return dict


listDir(image_dir)


def get_name(cmpt):
    try:
        name = names[cmpt]
        return name
    except:
        return "Empty Case"


def get_nbrHab():
    try:
        nbr = len(names)
        return nbr
    except:
        pass


global compteur
compteur = 0

root = tk.Tk()
root.geometry('420x230')
root.geometry('+500+280')
root.title("Logging")

myFrame = tk.Frame(root, bd=0, bg='#303030')
myFrame.place(relx=0,rely=0, relwidth=1,relheight=1)

label = tk.Label(myFrame, text=get_name(0))
label.pack(pady=10, padx=10)

button1 = ttk.Button(myFrame, text="Next", width=7, command = lambda: avancer())
button1.place(relx=0.8, rely=0.9)
button2 = ttk.Button(myFrame, text="Back", width=7, command = lambda: reculer())
button2.place(relx=0.1, rely=0.9)
imgs = []
resizing = []
finals = []
try:
    for i in range(get_nbrHab()):
        imgs.append(Image.open(image_dir + "/" + get_name(compteur) + "/1.jpg"))
        resizing.append(imgs[i].resize((160,120), Image.ANTIALIAS))
        finals.append(ImageTk.PhotoImage(resizing[i]))
except:
    pass

def avancer():
    label.config(text=get_name(compteur))
    print(compteur)
    label_img.config(image=finals[compteur])
    label_img.image=finals[compteur]
    compteur += 1
    print(compteur)
    print(finals)

def reculer():
    compteur-=1
    print(compteur)

label_img = tk.Label(myFrame, bg='white', image= finals[0])
label_img.image = finals[0]
label_img.place(relx=0.21, rely=0.15)



tk.mainloop()

