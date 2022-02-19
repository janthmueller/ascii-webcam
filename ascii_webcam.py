# https://www.youtube.com/watch?v=dTDgbx-XelY&ab_channel=SamiHatna

import sys
from copy import deepcopy

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pyvirtualcam
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def pixelate(frame):
    height, width = frame.shape[:2]
    pixel_width = int(width / pixel_size)
    pixel_height = int(height / pixel_size)
    temp = cv2.resize(frame, (pixel_width, pixel_height), interpolation=cv2.INTER_LINEAR)
    output_frame = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    return output_frame


def print_ascii_art(frame, new_frame):
    for x in range(pixel_size, frame_width + 1, pixel_size):
        for y in range(pixel_size, frame_height + 1, pixel_size):
            rgb = deepcopy(frame[int(y - pixel_size / 2), int(x - pixel_size / 2)])

            rgbv = rgb / 255
            lum = 0.2126 * rgbv[0] + 0.7152 * rgbv[1] + 0.0722 * rgbv[2]
            letter = letters[int(lum * (len(letters) - 1))]

            if ascii_mode == "real_color":
                cv2.putText(new_frame, letter, (x - pixel_size - 2, y - 2), cv2.FONT_HERSHEY_SIMPLEX, pixel_size / 24,
                            (int(rgb[0]), int(rgb[1]), int(rgb[2])))
            if ascii_mode == "single_color":
                cv2.putText(new_frame, letter, (x - pixel_size - 2, y - 2), cv2.FONT_HERSHEY_SIMPLEX, pixel_size / 24,
                            basic_color)
            if ascii_mode == "single_color_brightness":
                cv2.putText(new_frame, letter, (x - pixel_size - 2, y - 2), cv2.FONT_HERSHEY_SIMPLEX, pixel_size / 24,
                            np.array(basic_color) * lum)
            if ascii_mode == "color_map":
                cv2.putText(new_frame, letter, (x - pixel_size - 2, y - 2), cv2.FONT_HERSHEY_SIMPLEX, pixel_size / 24,
                            c_map[int(lum * (len(c_map) - 1))])


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("ASCII-Art Webcam")
        self.setWindowFlags(
            Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowMinimizeButtonHint)
        self.vbl = QVBoxLayout()

        self.feed_label = QLabel()
        self.vbl.addWidget(self.feed_label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(1, len(common_divisors) - 1)
        self.slider.setSingleStep(1)
        self.slider.valueChanged.connect(self.update_pixel_size)
        self.vbl.addWidget(self.slider)

        self.hbl = QHBoxLayout()
        self.vbl.addLayout(self.hbl)

        self.single_color_btn = QPushButton()
        self.single_color_btn.clicked.connect(self.set_single_color)
        self.hbl.addWidget(self.single_color_btn)

        self.single_color_brightness_btn = QPushButton()
        self.single_color_brightness_btn.clicked.connect(self.set_single_color_brightness)
        self.hbl.addWidget(self.single_color_brightness_btn)

        self.color_map_btn = QPushButton()
        self.color_map_btn.clicked.connect(self.set_color_map)
        self.hbl.addWidget(self.color_map_btn)

        self.real_color_btn = QPushButton()
        self.real_color_btn.clicked.connect(self.set_real_color)
        self.hbl.addWidget(self.real_color_btn)

        self.hbl1 = QHBoxLayout()
        self.vbl.addLayout(self.hbl1)

        self.ascii_edit = QLineEdit(letters)
        self.hbl1.addWidget(self.ascii_edit)

        self.ascii_edit_btn = QPushButton()
        self.ascii_edit_btn.clicked.connect(self.change_ascii)
        self.hbl1.addWidget(self.ascii_edit_btn)

        self.worker_1 = Worker()

        self.worker_1.start()
        self.worker_1.image_update.connect(self.image_update_slot)
        self.setLayout(self.vbl)

    def image_update_slot(self, image):
        self.feed_label.setPixmap(QPixmap.fromImage(image))

    def update_pixel_size(self, value):
        global pixel_size
        pixel_size = common_divisors[value]

    def set_single_color(self):
        global ascii_mode
        ascii_mode = "single_color"

    def set_real_color(self):
        global ascii_mode
        ascii_mode = "real_color"

    def set_single_color_brightness(self):
        global ascii_mode
        ascii_mode = "single_color_brightness"

    def set_color_map(self):
        global ascii_mode
        ascii_mode = "color_map"

    def change_ascii(self):
        global letters
        letters = self.ascii_edit.text()
        if len(letters) == 0: letters = ' '
        print(letters)


class Worker(QThread):
    image_update = pyqtSignal(QImage)

    def run(self):
        self.thread_active = True
        capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
        with pyvirtualcam.Camera(width=frame_width, height=frame_height, fps=20) as vcam:
            while self.thread_active:
                ret, frame = capture.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = cv2.flip(frame, 1)
                    new_frame = deepcopy(frame)
                    cv2.rectangle(new_frame, (0, 0), (frame_width, frame_height), bg_color, cv2.FILLED)
                    frame = pixelate(frame)
                    print_ascii_art(frame, new_frame)
                    pic = QImage(new_frame.data, new_frame.shape[1], new_frame.shape[0], QImage.Format_RGB888)
                    self.image_update.emit(pic)

                    vcam.send(new_frame)
                    vcam.sleep_until_next_frame()
            capture.release()

    def stop(self):
        self.thread_active = False
        self.quit()


if __name__ == "__main__":
    frame_width = 640
    frame_height = 480
    common_divisors = [i for i in range(1, min(frame_width, frame_height) + 1) if
                       frame_width % i == 0 and frame_height % i == 0]

    c_map = [np.array(plt.cm.jet(i / 1000)) * 255 for i in range(0, 1001)]
    letters = 'helloworld'
    ascii_mode = "single_color"
    pixel_size = common_divisors[1]
    basic_color = (0, 255, 0)
    bg_color = (0, 0, 0)

    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())
