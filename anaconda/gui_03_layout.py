# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:10:48 2020

@author: USER
"""


# 레이아웃
# 절대적 배치(Absolute positioning) (개발자가 마음대로 배치할수 있게 함)
# 단점 - 창의 크기가 변환되었을때 자동으로 위치가 변하지 않는다.
# 다양한 플롯에서 쓰려면 box레이아웃 그리드 레이아웃 사용.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20,60)
        
        btn1 = QPushButton('Button1',self)
        btn1.move(80,13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80,53)
        
        
        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)   # 새창 만들려면 어플리케이션 객체 무조건 만들어줘야한다.
    ex = MyApp()
    sys.exit(app.exec_())  