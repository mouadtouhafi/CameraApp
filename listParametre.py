import tkinter as tk
from tkinter import ttk
import subprocess
from PIL import ImageTk, Image

LARGE_FONT = ("Verdana", 12)

class MainUi(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("600x290")
        self.geometry("+100+20")
        self.title("Configuration")
        self.resizable(False, False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.place(relx=0,rely=0, relwidth=1, relheight=1)

    def Ajouter_Habt(self):
        cmd = 'python ajoutHabt.py'
        p = subprocess.Popen(cmd, shell=True)

    def Supprimer_Habt(self):
        cmd = 'python suppHabitant.py'
        p = subprocess.Popen(cmd, shell=True)

    def changer_pass(self):
        cmd = 'python changePassword.py'
        p = subprocess.Popen(cmd, shell=True)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='white')

        listPath = ["photos/config/ajtHabt.jpg", "photos/config/ajtVeh.jpg", "photos/config/suppHabt.jpg",
                    "photos/config/suppVeh.jpg", "photos/config/chgAdm.jpg", "photos/config/chgMdp.jpg"
                    ]

        listPath_logo = ["photos/config/addUser.jpg", "photos/config/addCar.jpg", "photos/config/deleteUser.jpg",
                          "photos/config/deleteCar.jpg", "photos/config/admin.jpg", "photos/config/changePassword.jpg"]


        x_size = 189
        y_size = 37

        img = []
        resized = []
        final = []
        label = []
        buttons = []

        for i in range(6):
            img.append(Image.open(listPath[i]))
            resized.append(img[i].resize((x_size, y_size), Image.ANTIALIAS))
            final.append(ImageTk.PhotoImage(resized[i]))

            label.append(tk.Label(self, image=final[i], bg='white'))
            label[i].image = final[i]

        for i in range(6):
            buttons.append(tk.Button(self, bg='white', activebackground='white', borderwidth=0))

        buttons[0].config(image=final[0], command=lambda : controller.Ajouter_Habt())
        buttons[1].config(image=final[1])
        buttons[2].config(image=final[2], command=lambda : controller.Supprimer_Habt())
        buttons[3].config(image=final[3])
        buttons[4].config(image=final[4])
        buttons[5].config(image=final[5], command=lambda : controller.changer_pass())

        buttons[0].place(x=8, y=100)
        buttons[1].place(x=205, y=100)
        buttons[2].place(x=8, y=240)
        buttons[3].place(x=205, y=240)
        buttons[4].place(x=402, y=100)
        buttons[5].place(x=402, y=240)

        img_logo = []
        resized_logo = []
        final_logo = []
        label_logo = []
        x_size_logo = [84,85,94,78,89,86]
        y_size_logo = [86,73,88,81,87,83]

        for i in range(6):
            img_logo.append(Image.open(listPath_logo[i]))
            resized_logo.append(img_logo[i].resize((x_size_logo[i], y_size_logo[i]), Image.ANTIALIAS))
            final_logo.append(ImageTk.PhotoImage(resized_logo[i]))

            label_logo.append(tk.Label(self, image=final_logo[i], bg='white'))
            label_logo[i].image = final_logo[i]

        label_logo[0].place(x=55, y=10)
        label_logo[1].place(x=260, y=15)
        label_logo[2].place(x=50, y=150)
        label_logo[3].place(x=265, y=155)
        label_logo[4].place(x=440, y=10)
        label_logo[5].place(x=450, y=155)


app = MainUi()
app.mainloop()
