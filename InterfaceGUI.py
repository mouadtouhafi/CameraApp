import tkinter as tk
import subprocess
from PIL import ImageTk, Image
import cv2
import pickle

LARGE_FONT = ("Verdana", 12)
face_cascade = cv2.CascadeClassifier("C://Users/poste/PycharmProjects/untitled2/data/haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name":1}
with open("labels.pickle",'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}


class MainUi(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("600x400")
        self.geometry("+100+20")
        self.title("Identification Faciale")
        self.resizable(False, False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.place(relx=0,rely=0, relwidth=1, relheight=1)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='white')

        listPath = ["photos/cadre.jpg", "photos/face_recog.jpg",
                    "photos/configuration.jpg", "photos/number-plate.jpg",
                    "photos/openCam1.jpg", "photos/openCam2.jpg",
                    "photos/Liste_habitants.jpg", "photos/Liste_vehicules.jpg",
                    "photos/administrateur.jpg", "photos/Logo.jpg", "photos/lancerSys.jpg",
                    "photos/arretSys.jpg"]

        x_size = [250,155,175,155,152,152,228,228,228,368,157,157]
        y_size = [220,134,42,155,36,36,45,45,45,93,36,36]

        img = []
        resized = []
        final = []
        label = []
        self.buttons = []

        for i in range(12):
            img.append(Image.open(listPath[i]))
            resized.append(img[i].resize((x_size[i], y_size[i]), Image.ANTIALIAS))
            final.append(ImageTk.PhotoImage(resized[i]))

            label.append(tk.Label(self, image=final[i], bg='white'))
            label[i].image=final[i]

        label[0].place(x=298, y=100)
        label[1].place(x=25, y=20)
        label[3].place(x=22, y=200)
        label[9].place(x=184, y=5)

        for i in range(8):
            self.buttons.append(tk.Button(self, bg='white', activebackground='white', borderwidth=0))

        self.buttons[0].config(image=final[2], command=lambda: self.config_clicked())
        self.buttons[1].config(image=final[4], command=lambda: self.openCam_clicked())
        self.buttons[2].config(image=final[5], command=lambda: self.openCam_clicked())
        self.buttons[3].config(image=final[6])
        self.buttons[4].config(image=final[7])
        self.buttons[5].config(image=final[8])
        self.buttons[6].config(image=final[10], command=lambda : self.lancer_sys_clicked("lancer"))
        self.buttons[7].config(image=final[11], command=lambda : self.lancer_sys_clicked("fermer"))

        self.buttons[0].place(x=375, y=290)
        self.buttons[1].place(x=24, y=150)
        self.buttons[2].place(x=24, y=350)
        self.buttons[3].place(x=310, y=122)
        self.buttons[4].place(x=310, y=172)
        self.buttons[5].place(x=310, y=222)
        self.buttons[6].place(x=391, y=350)
        self.buttons[7].place(x=225, y=350)

    def config_clicked(self):
        cmd = 'python listParametre.py'
        p = subprocess.Popen(cmd, shell=True)

    p = None

    def lancer_sys_clicked(self, para):
        global p
        cmd = 'python LancementSys.py'
        try:
            if para == "lancer":
                p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
                self.buttons[6]["state"] = 'disabled'
            if para == "fermer":
                p.kill()
                self.buttons[6]["state"] = 'normal'
        except:
            pass

    def openCam_clicked(self):
        cmd = 'python test.py'
        p = subprocess.Popen(cmd, shell=True)

app = MainUi()
app.mainloop()
