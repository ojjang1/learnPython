# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:07:21 2020

@author: USER
"""


## QCalendarWidget
# 달력 만들어주는 위젯

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate

## QDate 달력의 날짜를 클릭하게 되면 그것을 string 로 갖고오기위한 모듈

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)   #글자와 글자 사이에 가로와 세로선이 나타나게 해준다.
        cal.clicked[QDate].connect(self.showDate)  #캘린더 객체도 버튼처럼 push시그널이 있다. 클릭하게되면 QDate객체를 만들어준다.

        self.lbl = QLabel(self)
        date = cal.selectedDate()  # 현제 선택된 날짜를 얻어내는 함수.
        self.lbl.setText(date.toString()) #select 함수는 QDate객체를 반환하기 때문에 tostring 으로 문자열로 만들어줌

        vbox = QVBoxLayout()   #달력을 위치시켜주기 위한 레이아웃
        vbox.addWidget(cal)   # 
        vbox.addWidget(self.lbl) 

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def showDate(self, date):       #클릭 시그널이 발행되면 호출하는 함수
        self.lbl.setText(date.toString())   #라벨에 클릭한 날짜를 보여주게 하기


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())