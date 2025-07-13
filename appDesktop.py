import tkinter as tk
from tkinter import *
import tkinter.font as font

def show_frame(frame):
    frame.tkraise()

window = tk.Tk()

window.title("my frame")
window.geometry('300x300')
window.minsize(200,200)

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='nsew')

#==========frame1===========
frame1_title = tk.Label(frame1, text='this is frame1', bg='red')
frame1_title.pack(fill='x')
frame1_btn = tk.Button(frame1, text='enter', command=lambda:show_frame(frame2))
frame1_btn.pack()

#==========frame2===========
frame2_title = tk.Label(frame2, text='this is frame2', bg='green')
frame2_title.pack(fill='x')
frame2_btn = tk.Button(frame2, text='enter', command=lambda:show_frame(frame3))
frame2_btn.pack()

#==========frame3===========
frame3_title = tk.Label(frame3, text='this is frame3', bg='yellow')
frame3_title.pack(fill='x')
frame3_btn = tk.Button(frame3, text='enter', command=lambda:show_frame(frame1))
frame3_btn.pack()
# buttonFont = font.Font(family='Helvetica', size=16, weight='bold')
# myButton = Button(frame1, text="click", padx=45, pady=8, activebackground='#22C856', bd=5, bg='#5F9570', font=buttonFont)
# myButton.pack()
show_frame(frame1)
window.mainloop()