import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from tkinter import ttk
import os
import subprocess

TITRE_FONT = ("Verdana", 12, "bold")
FORM_FONT = ("Arial", 12)
Error_FONT = ("Arial", 10)

class App:
      def __init__(self, window, window_title, video_source="photos/VidDemo.mp4"):
         self.window = window
         self.window.title(window_title)
         self.video_source = video_source

         # Création d'un objet qui sert à ouvrir la caméra
         self.vid = MyVideoCapture(self.video_source)

         # Create a canvas that can fit the above video source size
         self.canvas = tkinter.Canvas(window, width = 650, height = 500, bg='black')
         self.canvas.pack()

         ttk.Style().configure("TButton", relief="flat",background="#000")
         self.btn_ajouter = ttk.Button(window, text="Ajouter", width=15, command=lambda : self.submit())
         self.btn_ajouter.place(relx=0.635, rely=0.44)

         self.btn_takeVid = ttk.Button(window, text="Capture Vidéo", width=18, command = lambda : self.start_record())
         self.btn_takeVid["state"] = 'disabled'
         self.btn_takeVid.place(relx=0.44, rely=0.44)

         self.label_titre = tkinter.Label(window, text="Ajouter un habitant", font=TITRE_FONT, bg='black', fg='white')
         self.label_titre.place(relx=0.42, rely=0.02)

         self.label_msg = tkinter.Label(window, font=Error_FONT, bg='black')
         self.label_msg.place(relx=0.48, rely=0.39)

        #=========================================== Tableau des labels ===============================
         self.labels = []
         for i in range(5):
             self.labels.append(tkinter.Label(window, bg='black', fg='white'))
             self.labels[i].place(relx=0.42, rely=0.1+0.06*i)

         self.labels[0].config(text="Nom :", font = FORM_FONT)
         self.labels[1].config(text="Prénom :", font=FORM_FONT)
         self.labels[2].config(text="Sexe :", font = FORM_FONT)
         self.labels[3].config(text="Age :", font=FORM_FONT)
         self.labels[4].config(text="Téléphone : ", font = FORM_FONT)

         # =========================================== Tableau des entrées ==============================
         self.entries = []
         for i in range(4):
             self.entries.append(tkinter.Entry(window, width=25))
         self.entries[0].bind("<FocusIn>", self.callback_entry0focus)
         self.entries[1].bind("<FocusIn>", self.callback_entry1focus)
         self.entries[2].bind("<FocusIn>", self.callback_entry2focus)
         self.entries[3].bind("<FocusIn>", self.callback_entry3focus)
         for i in range(4):
             if i == 2:
                 self.entries[i].place(relx=0.62, rely=0.105 + 0.06 * 2 * i)
             else:
                 self.entries[i].place(relx=0.62, rely=0.105 + 0.06 * i)
         self.s=tkinter.StringVar()
         ttk.Style().configure("TRadiobutton", background="#000", foreground='white')
         self.radio_button1 = ttk.Radiobutton(window, text="Masculin", variable=self.s, value="M")
         self.radio_button2 = ttk.Radiobutton(window, text="Féminin", variable=self.s, value="F")
         self.radio_button1.place(relx=0.615, rely=0.23)
         self.radio_button2.place(relx=0.76, rely=0.23)

         #=========================================== Boutons clavier =================================
         self.Style = ttk.Style()
         self.Style.configure('my.TButton', font=('Helvetica', 12))

         self.Lettre_L1 = ['a','z','e','r','t','y','u','i','o','p']
         self.boutons_L1 = []
         for i in range(10):
             self.boutons_L1.append(ttk.Button(window, text=self.Lettre_L1[i], width=3, style='my.TButton'))
             self.boutons_L1[i].place(relx=0.2+i*0.06, rely=0.62)

         self.Lettre_L2 = ['q','s','d','f','g','h','j','k','l','m']
         self.boutons_L2 = []
         for i in range(10):
             self.boutons_L2.append(ttk.Button(window, text=self.Lettre_L2[i], width=3, style='my.TButton'))
             self.boutons_L2[i].place(relx=0.2+i*0.06, rely=0.68)

         self.Lettre_L3 = ['w','x','c','v','b','n']
         self.boutons_L3 = []
         for i in range(6):
             self.boutons_L3.append(ttk.Button(window, text=self.Lettre_L3[i], width=3, style='my.TButton'))
             self.boutons_L3[i].place(relx=0.28 + i * 0.06, rely=0.74)

         self.Chiffre = ['0','1','2','3','4','5','6','7','8','9']
         self.boutons_C = []
         for i in range(10):
             self.boutons_C.append(ttk.Button(window, text=self.Chiffre[i], width=3, style='my.TButton'))
             self.boutons_C[i].place(relx=0.2 + i * 0.06, rely=0.82)

         self.Del_Bouton = ttk.Button(window, text='Effacer', width=7, style='my.TButton')
         self.Del_Bouton.place(relx=0.64, rely=0.74)

         self.boutons_C[0].config(command=lambda:self.button_clicked('0'))
         self.boutons_C[1].config(command=lambda:self.button_clicked('1'))
         self.boutons_C[2].config(command=lambda:self.button_clicked('2'))
         self.boutons_C[3].config(command=lambda:self.button_clicked('3'))
         self.boutons_C[4].config(command=lambda:self.button_clicked('4'))
         self.boutons_C[5].config(command=lambda:self.button_clicked('5'))
         self.boutons_C[6].config(command=lambda:self.button_clicked('6'))
         self.boutons_C[7].config(command=lambda:self.button_clicked('7'))
         self.boutons_C[8].config(command=lambda:self.button_clicked('8'))
         self.boutons_C[9].config(command=lambda:self.button_clicked('9'))

         self.boutons_L1[0].config(command=lambda:self.button_clicked('a'))
         self.boutons_L1[1].config(command=lambda:self.button_clicked('z'))
         self.boutons_L1[2].config(command=lambda:self.button_clicked('e'))
         self.boutons_L1[3].config(command=lambda:self.button_clicked('r'))
         self.boutons_L1[4].config(command=lambda:self.button_clicked('t'))
         self.boutons_L1[5].config(command=lambda:self.button_clicked('y'))
         self.boutons_L1[6].config(command=lambda:self.button_clicked('u'))
         self.boutons_L1[7].config(command=lambda:self.button_clicked('i'))
         self.boutons_L1[8].config(command=lambda:self.button_clicked('o'))
         self.boutons_L1[9].config(command=lambda:self.button_clicked('p'))

         self.boutons_L2[0].config(command=lambda:self.button_clicked('q'))
         self.boutons_L2[1].config(command=lambda:self.button_clicked('s'))
         self.boutons_L2[2].config(command=lambda:self.button_clicked('d'))
         self.boutons_L2[3].config(command=lambda:self.button_clicked('f'))
         self.boutons_L2[4].config(command=lambda:self.button_clicked('g'))
         self.boutons_L2[5].config(command=lambda:self.button_clicked('h'))
         self.boutons_L2[6].config(command=lambda:self.button_clicked('j'))
         self.boutons_L2[7].config(command=lambda:self.button_clicked('k'))
         self.boutons_L2[8].config(command=lambda:self.button_clicked('l'))
         self.boutons_L2[9].config(command=lambda:self.button_clicked('m'))

         self.boutons_L3[0].config(command=lambda:self.button_clicked('w'))
         self.boutons_L3[1].config(command=lambda:self.button_clicked('x'))
         self.boutons_L3[2].config(command=lambda:self.button_clicked('c'))
         self.boutons_L3[3].config(command=lambda:self.button_clicked('v'))
         self.boutons_L3[4].config(command=lambda:self.button_clicked('b'))
         self.boutons_L3[5].config(command=lambda:self.button_clicked('n'))

         self.Del_Bouton.config(command=lambda:self.effacer_text())

         # After it is called once, the update method will be automatically called every delay milliseconds
         self.delay = 1
         self.update()

         self.window.mainloop()

      Entry_choisit = '00'

      def start_record(self):
          self.window.destroy()
          cmd = 'python ajoutHabt2.py'
          p = subprocess.Popen(cmd, shell=True)
          out, err = p.communicate()

      def callback_entry0focus(self,event):
          self.Entry_choisit= 'E1'
      def callback_entry1focus(self,event):
          self.Entry_choisit= 'E2'
      def callback_entry2focus(self,event):
          self.Entry_choisit = 'E3'
      def callback_entry3focus(self,event):
          self.Entry_choisit = 'E4'

      def effacer_text(self):
          if self.Entry_choisit == 'E1':
              self.entries[0].delete(0, tkinter.END)
          if self.Entry_choisit == 'E2':
              self.entries[1].delete(0, tkinter.END)
          if self.Entry_choisit == 'E3':
              self.entries[2].delete(0, tkinter.END)
          if self.Entry_choisit == 'E4':
              self.entries[3].delete(0, tkinter.END)

      def button_clicked(self,charactere):
          if self.Entry_choisit=='E1':
              current = self.entries[0].get()
              self.entries[0].delete(0, tkinter.END)
              self.entries[0].insert(0, str(current) + str(charactere))
          if self.Entry_choisit=='E2':
              current = self.entries[1].get()
              self.entries[1].delete(0, tkinter.END)
              self.entries[1].insert(0, str(current) + str(charactere))
          if self.Entry_choisit=='E3':
              current = self.entries[2].get()
              self.entries[2].delete(0, tkinter.END)
              self.entries[2].insert(0, str(current) + str(charactere))
          if self.Entry_choisit=='E4':
              current = self.entries[3].get()
              self.entries[3].delete(0, tkinter.END)
              self.entries[3].insert(0, str(current) + str(charactere))


      def update(self):
         # Get a frame from the video source
         ret, frame = self.vid.get_frame()
         r_width = int(self.vid.width / 2)
         r_height = int(self.vid.height / 2)

         if ret:
             received_img = PIL.Image.fromarray(frame)
             resised = received_img.resize((r_width,r_height), PIL.Image.ANTIALIAS)
             self.photo = PIL.ImageTk.PhotoImage(image = resised)
             self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
         self.window.after(self.delay, self.update)

      file = open('C://Users/poste/Desktop/FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM/test.txt', "a")
      # Habitants = []

      def disable_ajouter(self):
          self.btn_ajouter["state"] = 'disabled'
      def submit(self):
          #=================================Pour continuer sur l'id précedent=======================================
          try:
              file = open('C://Users/poste/Desktop/FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM/test.txt', "r")
              line_count = 0
              for line in file:
                  if line != "\n":
                      line_count += 1
              file.close()
          except:
              return
        #===========================================================================================================
          # print("Number of lines in my file : " + str(line_count))

          Nom = self.entries[0].get()
          Prenom = self.entries[1].get()
          Age = self.entries[3].get()
          Tel = self.entries[2].get()

          def IsAgeNum(Age):
              try:
                  int(Age)
                  return True
              except:
                  return False

          def StrAge2Int():
              try:
                  converted_age=int(Age)
                  return converted_age
              except:
                  return 0

          def IsPhoneNum(Tel):
              try:
                  int(Tel)
                  return True
              except:
                  return False

          if len(Nom)<2 or len(Prenom)<2 or IsAgeNum == False or StrAge2Int()>120 or StrAge2Int()==0 or IsPhoneNum==False or len(Tel)!=10:
              self.label_msg.config(text = "Informations Invalides", fg='red')

          else:
              file1 = open('C://Users/poste/Desktop/FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM/test.txt', 'r')
              Lines = file1.readlines()
              count = 0
              list_noms = []
              list_prenoms = []
              for l in Lines:
                  count += 1
                  a = "Line{}: {}".format(count, l.strip())
                  for word in a.split():
                      # displaying the words
                      if word.__contains__('-'):
                          list_noms.append(word)
                      if word.__contains__('_'):
                          list_prenoms.append(word)

              if Nom + '-' in list_noms and Prenom + '_' in list_prenoms:
                   self.label_msg.config(text="Habitant déjà existant", fg='red')
              else:
                   self.label_msg.config(text="Habitant ajouté avec succés", fg='green')
                   line = "ID : " + str(line_count + 1) + "  " + Nom + "-  " + Prenom + "_  " + Age + "*" + "  " + Tel + "/" + "  " + self.s.get()+"#"
                   with open('C://Users/poste/Desktop/FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM/test.txt', 'a') as f:
                       f.writelines("\n")
                       f.writelines("".join(line))
                      # print(len(self.Habitants))
                   path = 'C://Users/poste/Desktop/' + Nom + '_' + Prenom
                   try:
                        os.mkdir(path)
                   except OSError:
                        print("Creation of the directory %s failed" % path)
                   else:
                        print("Successfully created the directory %s " % path)
                   self.disable_ajouter()
                   self.btn_takeVid["state"] = 'normal'

class MyVideoCapture:
     def __init__(self, video_source="photos/VidDemo.mp4"):
         # Open the video source
         self.vid = cv2.VideoCapture(video_source)
         self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
         self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

     def get_frame(self):
         if self.vid.isOpened():
             ret, frame = self.vid.read()
             if ret:
                 # Return a boolean success flag and the current frame converted to BGR
                 return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
             else:
                 self.vid = cv2.VideoCapture("photos/VidDemo.mp4")
                 return(ret, None)

             # Release the video source when the object is destroyed
     def __del__(self):
         if self.vid.isOpened():
             self.vid.release()

# Create a window and pass it to the Application object
App(tkinter.Tk(), "Ajouter des habitants")