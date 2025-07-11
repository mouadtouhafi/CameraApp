import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os

BASE_DIR = os.path.dirname(os.path.relpath(__file__))
image_dir = os.path.join(BASE_DIR, "my_training_face")

class MainUi(tk.Tk):
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

    def get_name(self, cmpt):
        try:
            self.name = names[cmpt]
            return self.name
        except:
            return "Empty Case"

    def get_nbrHab(self):
        try:
            self.nbr = len(names)
            return self.nbr
        except:
            pass

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("300x320")
        self.geometry("+500+100")
        self.title("Liste des habitants")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    global Ages
    global Tels
    global gender
    global dict_p


    Ages = []
    Tels = []
    gender = []
    dict_p = {}

    def get_Other_Infos(self):
        with open('C://Users/poste/Desktop/FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM/test.txt', 'r') as file:
            count=0
            for line in file:
                count+=1
                if count==1:
                    pass
                for word in line.split():
                    if word.__contains__('*'):
                        age = word.strip('*')
                        Ages.append(age)
                    if word.__contains__('/'):
                        tel = word.strip('/')
                        Tels.append(tel)
                    if word.__contains__('#'):
                        sexe = word.strip('#')
                        gender.append(sexe)
            for i in range(count-1):
                dict_p[i+1] = (Ages[i], Tels[i], gender[i])
        return dict_p




class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#A6A5A5')
        self.label = tk.Label(self, text=MainUi.get_name(self,0), font=('Arial',12), bg='#A6A5A5')
        self.label.pack(pady=5)

        self.label_age = tk.Label(self, text="Âge : " + MainUi.get_Other_Infos(self).get(1)[0], bg='#A6A5A5', font=('Arial',12))
        self.label_age.pack()

        self.label_tel = tk.Label(self, text="Tél : " + MainUi.get_Other_Infos(self).get(1)[1], bg='#A6A5A5', font=('Arial', 12))
        self.label_tel.pack(pady=5)

        self.label_sexe = tk.Label(self, text="Sexe : " + MainUi.get_Other_Infos(self).get(1)[2], bg='#A6A5A5', font=('Arial', 12))
        self.label_sexe.pack()

        self.Style = ttk.Style()
        self.Style.configure('my.TButton', font=('Helvetica', 10), background='#A6A5A5')

        button1 = ttk.Button(self, text="Next", width=9, style='my.TButton', command = lambda: self.next_clicked())
        button1.place(relx=0.71, rely=0.88)
        button2 = ttk.Button(self, text="Back", width=9, style='my.TButton', command = lambda: self.back_clicked())
        button2.place(relx=0.06, rely=0.88)
        self.imgs = []
        self.resizing = []
        self.finals = []
        self.compteur = 0

        for i in range(MainUi.get_nbrHab(self)):
            self.imgs.append(Image.open(image_dir + "/" + MainUi.get_name(self, i) + "/1.jpg"))
            self.resizing.append(self.imgs[i].resize((160,120), Image.ANTIALIAS))
            self.finals.append(ImageTk.PhotoImage(self.resizing[i]))

        self.ImageX = Image.open("photos/ShowUsers/1.jpg")
        self.res_X = self.ImageX.resize((160, 130), Image.ANTIALIAS)
        self.Unk = ImageTk.PhotoImage(self.res_X)

        self.label_img = tk.Label(self, bg='white', image= self.finals[0], bd=0)
        self.label_img.image = self.finals[0]
        self.label_img.pack(pady=10)

    def next_clicked(self):
        self.compteur += 1
        self.config()

    def back_clicked(self):
        if self.compteur > 0 :
            self.compteur-=1
            self.config()

    def config(self):
        try:
            self.label.config(text=MainUi.get_name(self, self.compteur))
            self.label_img.config(image=self.finals[self.compteur])
            self.label_age.config(text="Âge : " + MainUi.get_Other_Infos(self).get(self.compteur+1)[0])
            self.label_tel.config(text="Tél : " + MainUi.get_Other_Infos(self).get(self.compteur + 1)[1])
            self.label_sexe.config(text="Sexe : " + MainUi.get_Other_Infos(self).get(self.compteur + 1)[2])
        except:
            self.label_img.config(image=self.Unk)
            self.label_age.config(text="Âge : " )
            self.label_tel.config(text="Tél : " )
            self.label_sexe.config(text="Sexe : " )

app = MainUi()
app.mainloop()