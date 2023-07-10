
import time
import cv2
import threading
import datetime
import time
import tkinter
import PIL
import PIL.Image, PIL.ImageTk
from screeninfo import get_monitors
class status_webcam():
    def __init__(self,adress) -> None:
        self.adress = adress
        self.status_camera()
    def process_video(self,camera) -> tuple[bool,any]:
        (self.grabbed, self.frame) = camera.read()
        if not self.grabbed:
            print("disconnected!")
            return[self.grabbed,self.frame]
        else:
            return [self.grabbed,self.frame]
    def disconect(self):
        print("Camera not opened " +
        datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S%p"))
        self.a.x = False
        self.a.frame = None
        self.camera.release()
    def status_camera(self):
        self.a = gui()
        while 1:
            self.camera = cv2.VideoCapture(self.adress)
            if self.camera.isOpened():
                print("[INFO] Camera connected at " +
                    datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S%p"))
                while 1:
                    x,frame = self.process_video(self.camera)
                    try:
                        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                    except:
                        self.disconect()
                        time.sleep(2)
                        break
                    else: 
                        self.a.frame = frame
                        self.a.x = True
            self.disconect()
            time.sleep(5)
            continue
class gui():
    def __init__(self,frame=None,x=False) -> None:
        self.x = x
        self.frame = frame
        self.fps = 30
        self.lock = lock
        a = get_monitors()
        self.rsize = (a[0].width,a[0].height)      
        t_show = threading.Thread(target=self.show)
        t_show.start()

    def show(self):
        self.root = tkinter.Tk()
        self.root.attributes("-fullscreen", True) 
        self.canvas = tkinter.Canvas(self.root)
        self.canvas.pack(expand=True, fill=tkinter.BOTH)
        self.bg = self.canvas.create_image(0, 0, anchor = tkinter.NW,)
        self.image_erorr = self.fill_image()
        self.update()
        self.root.mainloop()
    def update(self):
        if self.x:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.frame))
            self.canvas.itemconfig(self.bg,image = self.photo)
            self.canvas.pack(fill="both",expand=True)
            time.sleep(1/self.fps)
            self.root.after(1, self.update)
        else:
            
            self.canvas.itemconfig(self.bg,image = self.image_erorr)
            self.canvas.pack(fill="both",expand=True)
            time.sleep(1)      
            self.root.after(1, self.update)
    def fill_image(self):
        scr_img = PIL.Image.open('colorbar.png')
        return PIL.ImageTk.PhotoImage(scr_img.resize(self.rsize))  
def status_():
    status_webcam("rtsp://192.168.31.86:8554/mystream")
lock = threading.Lock()
t_status = threading.Thread(name="status_camera",target=status_)
t_status.start()
