import cv2
from tkinter import *

# Khởi tạo đối tượng VideoCapture để truy cập webcam
cap = cv2.VideoCapture("rtsp://192.168.31.86:8554/mystream")  # Số 0 đại diện cho webcam mặc định

# Kiểm tra xem webcam đã sẵn sàng hay chưa
if not cap.isOpened():
    print("Không thể mở webcam")
    exit()

# Vòng lặp để đọc và hiển thị video từ webcam
while True:
    # Đọc frame từ webcam
    ret, frame = cap.read()

    # Kiểm tra xem việc đọc frame có thành công hay không
    if not ret:
        print("Không thể đọc frame từ webcam")
        break

    # Hiển thị frame
    cv2.imshow('Webcam', frame)

    # Thoát vòng lặp khi nhấn phím 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Giải phóng webcam và đóng cửa sổ hiển thị
cap.release()
cv2.destroyAllWindows()
