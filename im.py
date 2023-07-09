import tkinter
import cv2
import time
import PIL.Image, PIL.ImageTk
import tkinter.messagebox
class MyVideoCapture:
    def __init__(self, video_source):
        self.vid = cv2.VideoCapture(video_source)
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    def get_frame(self):
        if self.vid.isOpened():
            if not self.vid.isOpened():
                raise ValueError("Unable to open video source",self.video_source)
            ret, frame = self.vid.read()
            frame = cv2.resize(frame,(640,480))
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret,None)

class App:
    def __init__(self, window, window_title,video_source = 0, fpsLimit = 30):

        self.window = window
        self.window.title(window_title)
        #window.attributes('-fullscreen', True)
        self.video_source = video_source
        self.fpsLimit = fpsLimit

        self.vid = MyVideoCapture(video_source)    
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()
        self.delay = 1
        self.update()
        self.window.mainloop()
    def update(self):
        ret, frame = self.vid.get_frame()
        if ret:
            print('getphoto')
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
        self.window.after(self.delay, self.update)
        
# def check_key(event):
#     if event.keysym == 'q':
#         root.quit()

App(tkinter.Tk(),"CCTV","rtsp://192.168.31.86:8554/mystream")