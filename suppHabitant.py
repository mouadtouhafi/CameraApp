import tkinter as tk
from tkinter import ttk
import os

LARGE_FONT = ("Verdana", 12)
Medium_FONT = ("Verdana", 10, "bold")
Found_FONT = ("Verdana", 10)

BASE_DIR = os.path.dirname(os.path.relpath(__file__))
image_dir = os.path.join(BASE_DIR, "my_training_face")

class MainUi(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("350x300")
        self.geometry("+100+20")
        self.title("Supprimer habitant")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.place(relx=0,rely=0, relwidth=1, relheight=1)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='black')
        # self.master.configure(background='black')
        label = tk.Label(self, text="Supprimer un habitant : ", font = LARGE_FONT, fg='white', bg='black').place(x=35, y=20)
        label_nom = tk.Label(self, text="Nom : ", font = Medium_FONT, fg='white', bg='black').place(x=20, y=51)
        label_prenom = tk.Label(self, text="Prénom : ", font = Medium_FONT, fg='white', bg='black').place(x=20, y=80)

        self.entry1 = tk.Entry(self, width=30)
        self.entry1.bind("<FocusIn>", self.callback_entry1focus)
        self.entry1.place(x=98, y=53)
        self.entry2 = tk.Entry(self, width=30)
        self.entry2.bind("<FocusIn>", self.callback_entry2focus)
        self.entry2.place(x=98, y=80)

        self.label_check = tk.Label(self, font=Found_FONT, bg='black')
        self.label_check.place(x=100, y=270)


        Style = ttk.Style()
        Style.configure('my.TButton', font=('Helvetica', 12), background="#000", padding=0)

        self.button = ttk.Button(self, text="Vérifier", style='my.TButton', command=lambda : self.check())
        self.button.place(x=40, y=110)

        self.button1 = ttk.Button(self, text="Supprimer", style='my.TButton', command=lambda : self.supprimer())
        self.button1.place(x=180, y=110)
        self.button1["state"] = 'disabled'

        Lettre_L1 = ['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o']
        boutons_L1 = []
        for i in range(9):
            boutons_L1.append(ttk.Button(self, text=Lettre_L1[i], width=3, style='my.TButton'))
            boutons_L1[i].place(x=20+i*34, y=160)

        Lettre_L2 = ['p','q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        boutons_L2 = []
        for i in range(10):
            boutons_L2.append(ttk.Button(self, text=Lettre_L2[i], width=3, style='my.TButton'))
            boutons_L2[i].place(x=5+i*34, y=190)

        Lettre_L3 = ['m','w', 'x', 'c', 'v', 'b', 'n']
        boutons_L3 = []
        for i in range(7):
            boutons_L3.append(ttk.Button(self, text=Lettre_L3[i], width=3, style='my.TButton'))
            boutons_L3[i].place(x=32+i*34, y=220)

        boutons_del = ttk.Button(self, text="Del", width=4, style='my.TButton', command=lambda : self.effacer_text()).place(x=270, y=220)

        boutons_L1[0].config(command=lambda: self.button_clicked('a'))
        boutons_L1[1].config(command=lambda: self.button_clicked('z'))
        boutons_L1[2].config(command=lambda: self.button_clicked('e'))
        boutons_L1[3].config(command=lambda: self.button_clicked('r'))
        boutons_L1[4].config(command=lambda: self.button_clicked('t'))
        boutons_L1[5].config(command=lambda: self.button_clicked('y'))
        boutons_L1[6].config(command=lambda: self.button_clicked('u'))
        boutons_L1[7].config(command=lambda: self.button_clicked('i'))
        boutons_L1[8].config(command=lambda: self.button_clicked('o'))

        boutons_L2[0].config(command=lambda: self.button_clicked('p'))
        boutons_L2[1].config(command=lambda: self.button_clicked('q'))
        boutons_L2[2].config(command=lambda: self.button_clicked('s'))
        boutons_L2[3].config(command=lambda: self.button_clicked('d'))
        boutons_L2[4].config(command=lambda: self.button_clicked('f'))
        boutons_L2[5].config(command=lambda: self.button_clicked('g'))
        boutons_L2[6].config(command=lambda: self.button_clicked('h'))
        boutons_L2[7].config(command=lambda: self.button_clicked('j'))
        boutons_L2[8].config(command=lambda: self.button_clicked('k'))
        boutons_L2[9].config(command=lambda: self.button_clicked('l'))

        boutons_L3[0].config(command=lambda: self.button_clicked('m'))
        boutons_L3[1].config(command=lambda: self.button_clicked('w'))
        boutons_L3[2].config(command=lambda: self.button_clicked('x'))
        boutons_L3[3].config(command=lambda: self.button_clicked('c'))
        boutons_L3[4].config(command=lambda: self.button_clicked('v'))
        boutons_L3[5].config(command=lambda: self.button_clicked('b'))
        boutons_L3[6].config(command=lambda: self.button_clicked('n'))

        self.firstName = ""
        self.lastName = ""

    Entry_choisit = '00'

    def callback_entry1focus(self, event):
        self.Entry_choisit = 'E1'

    def callback_entry2focus(self, event):
        self.Entry_choisit = 'E2'

    def button_clicked(self, charactere):
        if self.Entry_choisit == 'E1':
            current = self.entry1.get()
            self.entry1.delete(0, tk.END)
            self.entry1.insert(0, str(current) + str(charactere))
        if self.Entry_choisit == 'E2':
            current = self.entry2.get()
            self.entry2.delete(0, tk.END)
            self.entry2.insert(0, str(current) + str(charactere))

    def check(self):
        Nom = self.entry1.get()
        Prenom = self.entry2.get()
        self.firstName=Nom
        self.lastName=Prenom
        var = 0
        with open('C://Users/poste/Desktop/FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM/test.txt', "r") as f:
            for line in f:
                for word in line.split():
                    if word == Nom+'-' :
                        var += 1
                    if word == Prenom+'_':
                        var += 1
                    if var == 2:
                        break
        print(var)
        if var==2:
            self.label_check.config(text="Habitant trouvé", fg='green')
            self.button["state"] = 'disabled'
            self.button1["state"] = 'normal'
            self.entry1.config(state='disabled')
            self.entry2.config(state='disabled')
        if var!=2:
            self.label_check.config(text="Habitant non trouvé", fg='red')

    def supprimer(self):
        file = open('C://Users/poste/Desktop/FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM/test.txt', "r")
        Lines = file.readlines()
        count = 0
        file.close()

        file = open('C://Users/poste/Desktop/FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM/test.txt', "w")
        file.close()

        file = open('C://Users/poste/Desktop/FACE RECOGNITION BASED ATTENDANCE MONITORING SYSTEM/test.txt', "w")
        for line in Lines:
            count += 1
            if not self.firstName + '-' in line.split() or not self.lastName + '_' in line.split():
                # print('ues')
                file.writelines("".join(line))
            # if not self.firstName + '-' in line.split():
            #     if not self.lastName + '_' in line.split():
            #         file.writelines("".join(line))
        file.close()
        self.label_check.config(text="Habitant supprimé", fg='green')
        name_path = os.path.join("C://Users/poste/Desktop/", self.firstName+'_'+self.lastName)
        os.rmdir(name_path)
        print("% s has been removed successfully" % self.lastName+'_'+self.firstName)



    def effacer_text(self):
        if self.Entry_choisit == 'E1':
            self.entry1.delete(0, tk.END)
        if self.Entry_choisit == 'E2':
            self.entry2.delete(0, tk.END)

app = MainUi()
app.mainloop()
