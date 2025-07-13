import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
import pickle
from tkinter import ttk
from tkinter.font import Font

face_cascade = cv2.CascadeClassifier("C://Users/poste/PycharmProjects/untitled2/data/haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name":1}


with open("labels.pickle",'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

class App:
      def __init__(self, window, window_title, geometry, video_source=0):
          self.window = window
          self.window.title(window_title)
          self.video_source = video_source
          self.geometry=geometry

         # open video source (by default this will try to open the computer webcam)
          self.vid = MyVideoCapture(self.video_source)

         # Create a canvas that can fit the above video source size
          self.canvas = tkinter.Canvas(window, width = 830, height = self.vid.height+20, bd=10)
          self.canvas.pack()

         # Button that lets the user take a snapshot
          self.btn_snapshot=ttk.Button(window, text="Prendre une Capture d'écran", command=self.snapshot, width=40)
          self.btn_snapshot.place(relx=0.25, rely=0.935)

          self.btn_exit = ttk.Button(window, text="Sortir", command=self.Close, width=15)
          self.btn_exit.place(relx=0.85, rely=0.935)

          self.label_0 = tkinter.Label(window, text="Personnes détectées :", font=('Arial Rounded MT Bold', 12))
          self.label_0.place(relx=0.76, rely=0.1)

          self.present = self.vid.name_id
          self.label_1=tkinter.Label(window, text=" ", font=('Arial Rounded MT Bold',15))
          self.label_1.place(relx=0.77, rely=0.15)
          self.update_label()

         # After it is called once, the update method will be automatically called every delay milliseconds
          self.delay = 15
          self.update()

          self.window.mainloop()

      def update_label(self):
          self.label_1.configure(text=' {}'.format(labels[self.present]))
          self.label_1.after(200, self.update_label)
          self.present=self.vid.name_id

      def Close(self):
          self.window.destroy()

      def snapshot(self):
         # Get a frame from the video source
         ret, frame = self.vid.get_frame()

         if ret:
             cv2.imwrite("Captures/frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

      def update(self):
         # Get a frame from the video source
         ret, frame = self.vid.get_frame()

         if ret:
             self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
             self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

         self.window.after(self.delay, self.update)


class MyVideoCapture:
     def __init__(self, name_id, video_source=0):
         # Open the video source
         self.vid = cv2.VideoCapture(video_source,cv2.CAP_DSHOW)
         if not self.vid.isOpened():
             raise ValueError("Unable to open video source", video_source)

         # Get video source width and height
         self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
         self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
         self.name_id=name_id

     def get_frame(self):


         if self.vid.isOpened():
             ret, frame = self.vid.read()
             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
             faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
             for (x, y, w, h) in faces:
                 # print (x,y,w,h)
                 roi_gray = gray[y:y + h, x:x + w]
                 roi_color = frame[y:y + h, x:x + w]
                 img_item = "C://Users/poste/Music/my_image.png"
                 cv2.imwrite(img_item, roi_gray)

                 id_,conf = recognizer.predict(roi_gray)

                 if conf >= 70:  # and conf <= 85:
                     print(conf)
                     # print(id_)
                     # print(labels[id_])
                     self.name_id=id_
                     # print(self.name_id)

                 color = (255, 0, 0)
                 stroke = 2
                 width = x + w
                 height = y + h
                 cv2.rectangle(frame, (x, y), (width, height), color, stroke)
             if ret:
                 # Return a boolean success flag and the current frame converted to BGR
                 return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
             else:
                 return (ret, None)
         else:
             return(ret, None)

     # Release the video source when the object is destroyed
     def __del__(self):
         if self.vid.isOpened():
             self.vid.release()

 # Create a window and pass it to the Application object
App(tkinter.Tk(), "Caméra 1 ", "800x650")