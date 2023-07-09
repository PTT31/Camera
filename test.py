import threading
import time
import cv2 as cv
import os
import tkinter
import PIL.Image, PIL.ImageTk
import tkinter.messagebox
class MyVideoCapture:
    def __init__(self, video_source):
        self.vid = cv.VideoCapture(video_source)
        self.width = self.vid.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    def get_frame(self):
        if self.vid.isOpened():
            if not self.vid.isOpened():
                raise ValueError("Unable to open video source",self.video_source)
            ret, frame = self.vid.read()
            frame = cv.resize(frame,(640,480))
            if ret:
                return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
            else:
                return (ret,None)

def check_ping():
    hostname = "192.168.31.86"
    response = os.system("ping -n 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
    print(pingstatus)
    return pingstatus
def show_video():
    def no_connect():
        image1 = PIL.Image.open("colorbar.png")
        test = PIL.ImageTk.PhotoImage(image1)

        label1 = tkinter.Label(image=test)
        label1.image = test

        # Position image
        label1.place(x=0, y=0)
    def update():
        try:
            ret, frame = vid.get_frame()
        except:
            no_connect()
        else:
            if ret:
                print('get photo')
                photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                canvas.create_image(0, 0, image = photo, anchor = tkinter.NW)
            root.after(1,update)
    if check_ping() == "Network Active":
        vid = MyVideoCapture("rtsp://192.168.31.86:8554/mystream")
        canvas = tkinter.Canvas(root,width=vid.width,height=vid.height)
        canvas.pack()
        update()
    else:
        no_connect()       
root = tkinter.Tk()
#root.attributes('-fullscreen', True)

print('loop')
show_video()
root.mainloop()