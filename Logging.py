import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from tkinter.font import Font
from PIL import ImageTk, Image
import subprocess

root = tk.Tk()
root.geometry('420x230')
root.geometry('+500+280')
root.title("Logging")

myFrame = tk.Frame(root, bd=0, bg='#303030')
myFrame.place(relx=0,rely=0, relwidth=1,relheight=1)

btnFrame = tk.Frame(myFrame, bd=0, bg='#303030')
btnFrame.place(x=230,y=55, relwidth=0.5,relheight=0.8)

def limitSize(*args):
    mdp = mdpValue.get()
    if len(mdp) > 4 :
        mdpValue.set(mdp[:4])

def getMdp():
    Pass = myEntry.get()
    read_pass = ""
    with open('txt_files/Password.txt') as f:
        read_pass = f.read()

    if Pass==read_pass:
        root.destroy()
        cmd = 'python listParametre.py'
        p = subprocess.Popen(cmd, shell=True)
    else:
        myEntry.delete(0, tk.END)

mdpValue = StringVar()
mdpValue.trace('w', limitSize)

myFont = Font(family="Arial Rounded MT Bold",
                 size=20,
                 weight="bold")

paths = ["photos/Clavier_num/1.jpg", "photos/Clavier_num/2.jpg", "photos/Clavier_num/3.jpg",
         "photos/Clavier_num/4.jpg", "photos/Clavier_num/5.jpg", "photos/Clavier_num/6.jpg",
         "photos/Clavier_num/7.jpg", "photos/Clavier_num/8.jpg", "photos/Clavier_num/9.jpg"]
photo = []
resized = []
final = []
bnt_labels = []
buttons = []

for i in range(9):
    photo.append(Image.open(paths[i]))
    resized.append(photo[i].resize((45,45), Image.ANTIALIAS))
    final.append(ImageTk.PhotoImage(resized[i]))

    bnt_labels.append(tk.Label(btnFrame, image=final[i], bg='#303030'))
    buttons.append(tk.Button(btnFrame, image=final[i], bg='#303030', activebackground='#303030', borderwidth=0))

buttons[0].place(x=10, y=2)
buttons[1].place(x=60, y=2)
buttons[2].place(x=110, y=2)
buttons[3].place(x=10, y=52)
buttons[4].place(x=60, y=52)
buttons[5].place(x=110, y=52)
buttons[6].place(x=10, y=102)
buttons[7].place(x=60, y=102)
buttons[8].place(x=110, y=102)

buttons[0].config(text="1", command=lambda: button_clicked(1))
buttons[1].config(text="2", command=lambda: button_clicked(2))
buttons[2].config(text="3", command=lambda: button_clicked(3))
buttons[3].config(text="4", command=lambda: button_clicked(4))
buttons[4].config(text="5", command=lambda: button_clicked(5))
buttons[5].config(text="6", command=lambda: button_clicked(6))
buttons[6].config(text="7", command=lambda: button_clicked(7))
buttons[7].config(text="8", command=lambda: button_clicked(8))
buttons[8].config(text="9", command=lambda: button_clicked(9))

def button_clicked(number):
    current = myEntry.get()
    myEntry.delete(0, tk.END)
    myEntry.insert(0, str(current) + str(number))

label = tk.Label(myFrame, text="Entrez le code", font=myFont, fg='white', bg='#303030')
label.place(x=10, y=14)

myEntry = tk.Entry(myFrame, font=('Arial Rounded MT Bold', 50), bd=0, bg='#303030', textvariable=mdpValue, width=4, justify='left', fg="green")
myEntry.place(x=30, y=50)

ttk.Style().configure("TButton", relief="flat",background='#303030', font=('Helvetica', 12, "bold"))
myButton = ttk.Button(myFrame, text="Entrer", width=10, command=getMdp)
myButton.place(x=60, y=140)


tk.mainloop()