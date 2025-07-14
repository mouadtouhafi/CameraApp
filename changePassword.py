import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from tkinter import ttk
import os
import subprocess

LARGE_FONT = ("Verdana", 10, "bold")
TITRE_FONT = ("Verdana", 15, "bold")

class App:
      def __init__(self, window, window_title):
         self.window = window
         self.window.title(window_title)


         # Create a canvas that can fit the above video source size
         self.canvas = tkinter.Canvas(window, width = 320, height = 285, bg='#93ABA3')
         self.canvas.pack()

         ttk.Style().configure("TButton", relief="flat",background='#93ABA3', font=('Helvetica', 9, "bold"))
         self.myButton = ttk.Button(window, text="Valider", width=10, command = lambda : self.submit())
         self.myButton.place(x=60, y=140)
         self.myButton2 = ttk.Button(window, text="Effacer", width=10, command = lambda : self.effacer())
         self.myButton2.place(x=60, y=170)
         self.myButton3 = ttk.Button(window, text="Fermer", width=10, command = lambda : self.sortir())
         self.myButton3.place(x=60, y=200)

         self.label_titre = tkinter.Label(window, text="Changer le code :", font=TITRE_FONT, bg="#93ABA3", fg="#8C1F1B")
         self.label_titre.place(x=60, y=6)
         self.label_mdpAncien = tkinter.Label(window, text="Tapez le code ancien :", fg='black', bg="#93ABA3",font=LARGE_FONT)
         self.label_mdpAncien.place(x=10, y=55)
         self.label_mdpNv1 = tkinter.Label(window, text="Tapez le nouveau code :", fg='black', bg="#93ABA3",font=LARGE_FONT)
         self.label_mdpNv1.place(x=10, y=81)
         self.label_mdpNv2 = tkinter.Label(window, text="Code ancien :", fg='black', bg="#93ABA3", font=LARGE_FONT)
         self.label_mdpNv2.place(x=10,y=107)
         self.label_Note = tkinter.Label(window, text="* Le code doit contenir 4 chiffres.", fg='white', bg="#93ABA3")
         self.label_Note.place(x=10, y=230)
         self.label_MSG = tkinter.Label(window, bg="#93ABA3")
         self.label_MSG.place(x=10, y=250)

         # =========================================== Tableau des entrées ==============================
         self.entries = []
         for i in range(3):
             self.entries.append(tkinter.Entry(window, width=12, font=('Arial Rounded MT Bold', 10), bd=0, justify='center', fg="green"))
         self.entries[0].bind("<FocusIn>", self.callback_entry0focus)
         self.entries[1].bind("<FocusIn>", self.callback_entry1focus)
         self.entries[2].bind("<FocusIn>", self.callback_entry2focus)

         self.entries[0].place(x=200, y=55)
         self.entries[1].place(x=200, y=81)
         self.entries[2].place(x=200, y=107)

         #=========================================== Boutons clavier =================================
         self.Style = ttk.Style()
         self.Style.configure('my.TButton', font=('Helvetica', 12))


         self.Chiffre = ['1','2','3','4','5','6','7','8','9']
         self.boutons_C = []
         for i in range(9):
             self.boutons_C.append(ttk.Button(window, text=self.Chiffre[i], width=3, style='my.TButton'))
         #     self.boutons_C[i].place(relx=0.2 + i * 0.06, rely=0.82)

         self.boutons_C[0].place(x=191, y=138)
         self.boutons_C[1].place(x=228, y=138)
         self.boutons_C[2].place(x=265, y=138)
         self.boutons_C[3].place(x=191, y=168)
         self.boutons_C[4].place(x=228, y=168)
         self.boutons_C[5].place(x=265, y=168)
         self.boutons_C[6].place(x=191, y=198)
         self.boutons_C[7].place(x=228, y=198)
         self.boutons_C[8].place(x=265, y=198)

         self.boutons_C[0].config(command=lambda:self.button_clicked('1'))
         self.boutons_C[1].config(command=lambda:self.button_clicked('2'))
         self.boutons_C[2].config(command=lambda:self.button_clicked('3'))
         self.boutons_C[3].config(command=lambda:self.button_clicked('4'))
         self.boutons_C[4].config(command=lambda:self.button_clicked('5'))
         self.boutons_C[5].config(command=lambda:self.button_clicked('6'))
         self.boutons_C[6].config(command=lambda:self.button_clicked('7'))
         self.boutons_C[7].config(command=lambda:self.button_clicked('8'))
         self.boutons_C[8].config(command=lambda:self.button_clicked('9'))

         # After it is called once, the update method will be automatically called every delay milliseconds
         self.delay = 1

         self.window.mainloop()

      Entry_choisit = '00'

      def callback_entry0focus(self,event):
          self.Entry_choisit= 'E1'
      def callback_entry1focus(self,event):
          self.Entry_choisit= 'E2'
      def callback_entry2focus(self,event):
          self.Entry_choisit = 'E3'

      def effacer(self):
          if self.Entry_choisit == 'E1':
              self.entries[0].delete(0, tkinter.END)
          if self.Entry_choisit == 'E2':
              self.entries[1].delete(0, tkinter.END)
          if self.Entry_choisit == 'E3':
              self.entries[2].delete(0, tkinter.END)

      def sortir(self):
          self.window.destroy()

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

      def submit(self):
          with open('txt_files/Password.txt') as f:
              read_pass = f.read()

          ancien = self.entries[0].get()
          nouveau1 = self.entries[1].get()
          nouveau2 = self.entries[2].get()

          if nouveau1 == nouveau2 and ancien==read_pass and len(nouveau1)==4:
              self.label_MSG.config(text="Code bien changé", fg='green')
              open('txt_files/Password.txt', 'w').close()
              with open('txt_files/Password.txt', 'w') as f:
                  f.write(nouveau1)
              self.myButton["state"] = 'disabled'
              self.myButton2["state"] = 'disabled'
          else:
              self.label_MSG.config(text="Erreur", fg='red')

App(tkinter.Tk(), "Réinitialiser le code")