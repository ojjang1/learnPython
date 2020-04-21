# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:37:13 2020

@author: USER
"""


## 이미지를 넣을때 사용하는 QPixmap

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

#QLabel 은 이미지의 가로와 세로의 pixel 을 구해서 표시해주기위해 불렀다.
# label 들을 정렬하는 상수도 Qt 가 갖고 있다.

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('hyo.jpg')

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        # 이미지의 사이즈를 구해서 라벨에 표시해 주겠다.
        lbl_size.setAlignment(Qt.AlignCenter)
        # 라벨들을 정렬하는데 가로로 정렬 시키겠다.

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        vbox.addWidget(lbl_size)
        self.setLayout(vbox)

        self.setWindowTitle('QPixmap')
        self.move(300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())