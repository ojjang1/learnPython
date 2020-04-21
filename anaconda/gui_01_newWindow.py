# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:09:26 2020

@author: USER
"""

# GUI 로 창 띄우기

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):    #상속받기
    
    def __init__(self):   #인스턴스로 사용하기위해 self 넣고
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("My First Application")   #창의 타이틀
        self.move(300,300)  # 창이 나타나는 위치
        self.resize(400,200)  #창의 크기 (weight,height)
        self.show()    #창 띄우기
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)   # 새창 만들려면 어플리케이션 객체 무조건 만들어줘야한다.
    ex = MyApp()
    sys.exit(app.exec_())    #시스템에 X 버튼을 누르면 실행되는 창을 닫아줘.

