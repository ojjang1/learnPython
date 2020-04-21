# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:38:32 2020

@author: USER
"""


# Qslider
# 마우스로 움직일 수 있는 슬라이더바.
# setTickInterval() 틱 간격 조절
# setTickPosition() 틱 위치 조절 (단위는 픽셀이 아닌 값)
# (수평)0 표시하지않음, 1 위, 2 아래, 3 양쪽에
# (수직) TicksAbove 왼쪽에, TickBelow 오른쪽에

# QDial
# 슬라이더를 둥근 형태로 표현한 위젯
# 다이얼은 틱 이아니고 노치 라고 함.
# setNotchesVisible(True )  노치를 표시 
# 슬라이드 와 시그널 ,슬롯, 메서드들을 공유함

# 시그널
# valueChanged() 슬라이더 값이 변할떄 발생
# sliderPressed() 슬라이더를 움직이기 시작할 때 발생
# sliderMobed() 슬라이더를 움직이면 발생
# sliderReleased() 슬라이더를 놓을 때 발생

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self)  
        #수평 슬라이더 생성, 생성시킬때 수평, 수직 설정. 상수는 Qt가 갖고있으니 임포트 해옴
        self.slider.move(30, 30)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2)
        # 싱글스탭 으로 하고 간격은 2
        
        self.dial = QDial(self)   #다이얼 객체 생성
        self.dial.move(30, 50)
        self.dial.setRange(0, 50)   #다이얼 범위 지적

        btn = QPushButton('Default', self)
        btn.move(35, 160)   

        self.slider.valueChanged.connect(self.dial.setValue)  #슬라이더 값 변화 일어난 후 다이얼 값도 동일하게(내장함수임)
        self.dial.valueChanged.connect(self.slider.setValue)  #다이얼의 값 변화가 일어난 후 슬라이더값도 동일하게(내장함수, 직접설정)
        btn.clicked.connect(self.button_clicked)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()
        
    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())