import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from tkinter import ttk
import numpy as np
import os, shutil
import PIL.Image, PIL.ImageTk
import subprocess

TITRE_FONT = ("Verdana", 12)
FONT1 = ("Verdana", 9)
FONT2 = ("Verdana", 8)

class App:
     def __init__(self, window, window_title, video_source=0):
         self.window = window
         self.window.title(window_title)
         self.video_source = video_source

         # open video source (by default this will try to open the computer webcam)
         self.vid = MyVideoCapture(self.video_source)

         # Create a canvas that can fit the above video source size
         self.canvas = tkinter.Canvas(window, width = 300, height = 300)
         self.canvas.pack()

         # Button that lets the user take a snapshot
         self.start_btn=ttk.Button(window, text="Prendre des images", width=28, command=lambda:self.record())
         self.start_btn.place(relx=0.21, rely=0.05)

         self.restart_btn=ttk.Button(window, text="Recommencer", width=28, command=lambda:self.effacer_contenu())
         self.restart_btn["state"] = 'disabled'
         self.restart_btn.place(relx=0.21, rely=0.20)

         self.fermer_btn = ttk.Button(window, text="Fermer", width=28, command=lambda: self.fermer())
         self.fermer_btn["state"] = 'disabled'
         self.fermer_btn.place(relx=0.21, rely=0.30)

         self.label = tkinter.Label(window, text="Nombre d'images captées :", font=TITRE_FONT)
         self.label.place(relx=0.03, rely=0.85)

         self.label_count = tkinter.Label(window, text="_", font=TITRE_FONT, fg='red')
         self.label_count.place(relx=0.8, rely=0.85)

         self.labelNote1 = tkinter.Label(window, text='Notes : ', font=TITRE_FONT)
         self.labelNote1.place(relx=0.02, rely=0.40)

         self.labelNote2 = tkinter.Label(window, text='Essayez de prendre des photos des différentes', font=FONT2)
         self.labelNote2.place(relx=0.04, rely=0.49)
         self.labelNote3 = tkinter.Label(window, text='faces de votre visages.', font=FONT2)
         self.labelNote3.place(relx=0.06, rely=0.55)
         self.labelNote4 = tkinter.Label(window, text='Essayez de bouger votre visage doucement.', font=FONT2)
         self.labelNote4.place(relx=0.04, rely=0.63)
         self.labelNote5 = tkinter.Label(window, text='Pour réessayer appuyez sur le bouton', font=FONT2)
         self.labelNote5.place(relx=0.04, rely=0.71)
         self.labelNote6 = tkinter.Label(window, text='recommencer.', font=FONT2)
         self.labelNote6.place(relx=0.06, rely=0.77)




         # After it is called once, the record method will be automatically called every delay milliseconds
         self.delay = 20
         self.window.mainloop()

     def disable_commencer(self):
         self.start_btn["state"] = 'disabled'

     def fermer(self):
         self.window.destroy()
         cmd = 'python training.py'
         p = subprocess.Popen(cmd, shell=True)

     def get_direc_name(self):
         file = open('C://Users/poste/Desktop/FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM/test.txt', "r")
         lineList = file.readlines()
         file.close()
         l = lineList[-1]
         words = l.split()
         nom = words[3].replace('-', '')
         prenom = words[4].replace('_', '')
         return nom+'_'+prenom

     def record(self):
         # Get a frame from the video source
         ret, frame = self.vid.get_frame()
         if ret:
             self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
             converted = frame.astype(np.float32)
             name = "C://Users/poste/Desktop/" + self.get_direc_name() + "/%d.jpg" % self.vid.count
             my_image = cv2.cvtColor(converted, cv2.COLOR_BGR2RGB)
             if self.vid.count <= 199:
                cv2.imwrite(name, my_image)
                self.vid.count+=1
                self.label_count.config(text=self.vid.count)
             else:
                 self.restart_btn["state"] = 'normal'
                 self.fermer_btn["state"] = 'normal'
                 self.start_btn["state"] = 'disabled'
         self.window.after(self.delay, self.record)

     def effacer_contenu(self):
         folder = "C://Users/poste/Desktop/" + self.get_direc_name()
         for filename in os.listdir(folder):
             file_path = os.path.join(folder, filename)
             try:
                 if os.path.isfile(file_path) or os.path.islink(file_path):
                     os.unlink(file_path)
                 elif os.path.isdir(file_path):
                     shutil.rmtree(file_path)
             except Exception as e:
                 print('echec de la suppression %s. raison: %s' % (file_path, e))
         self.disable_commencer()
         self.vid.count=0
         self.label_count.config(text=self.vid.count)


class MyVideoCapture:
     def __init__(self, video_source=0):
         # Open the video source
         self.vid = cv2.VideoCapture(video_source, cv2.CAP_DSHOW)
         if not self.vid.isOpened():
             raise ValueError("Unable to open video source", video_source)

         # Get video source width and height
         self.width = self.vid.set(3,320)
         self.height = self.vid.set(4,240)
         self.count=0


     def get_frame(self):
         if self.vid.isOpened():
             ret, frame = self.vid.read()
             if ret:
                 # Return a boolean success flag and the current frame converted to BGR
                 return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
             else:
                 return (ret, None)

     # Release the video source when the object is destroyed
     def __del__(self):
         if self.vid.isOpened():
             self.vid.release()

# Create a window and pass it to the Application object
app =App(tkinter.Tk(), "Ajouter Habitant")