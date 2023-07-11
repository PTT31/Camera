
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
        self.camera.release()
    def status_camera(self):
        self.a = gui()
        while 1:
            self.camera = cv2.VideoCapture(self.adress,cv2.CAP_GSTREAMER)
            if self.camera.isOpened():
                print("[INFO] Camera connected at " +
                    datetime.datetime.now().strftime("%m-%d-%Y %I:%M:%S%p"))
                while 1:
                    x,frame = self.process_video(self.camera)
                    try:
                        frame = cv2.cvtColor(cv2.resize(frame,self.a.rsize),cv2.COLOR_BGR2RGB)
                    except:
                        self.a.x = False
                        self.disconect()
                        time.sleep(10)
                        break
                    else: 
                        self.a.frame = frame
                        self.a.x = True
            self.disconect()
            time.sleep(10)
            continue
class gui():
    def __init__(self,frame=None,x=False) -> None:
        self.x = x
        self.frame = frame
        self.fps = 60
        self.lock = lock
        a = get_monitors()
        self.rsize = (a[0].width,a[0].height)     
        self.prev_frame_time = 0
        self.new_frame_time = 0 
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
        self.new_frame_time = time.time()
        fps = 1/(self.new_frame_time-self.prev_frame_time)
        fps = int(fps)
        fps = str(fps)
        self.prev_frame_time = self.new_frame_time
        if self.x:
            cv2.putText(self.frame, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.frame))
            self.canvas.itemconfig(self.bg,image = self.photo)
            # time.sleep(1/self.fps-0.001)
            self.root.after(1, self.update)
        else:
            print(fps)
            self.canvas.itemconfig(self.bg,image = self.image_erorr)
            self.root.after(1000, self.update)
    def fill_image(self):
        scr_img = PIL.Image.open('colorbar.png')
        return PIL.ImageTk.PhotoImage(scr_img.resize(self.rsize))  
def status_():
    status_webcam("souphttpsrc location=http://127.0.0.1:11470/dd0ae9420a62bfd75e97d2e6b7443c556599c67a/0 ! NVD3D11 ! videoconvert ! video/x-raw,format=BGR ! appsink")
lock = threading.Lock()
t_status = threading.Thread(name="status_camera",target=status_)
t_status.start()
