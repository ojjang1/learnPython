# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:29:16 2020

@author: USER
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):    #상속받기
    
    def __init__(self):   #인스턴스로 사용하기위해 self 넣고
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Icon")   #창의 타이틀
        self.setWindowIcon(QIcon('web.png'))  #어플리케이션 아이콘을 설정
        self.setGeometry(300,300,300,200)
        self.show()    #창 띄우기
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)   # 새창 만들려면 어플리케이션 객체 무조건 만들어줘야한다.
    ex = MyApp()
    sys.exit(app.exec_())    #시스템에 X 버튼을 누르면 실행되는 창을 닫아줘.

#self.setWindowIcon(QIcon('web.png'))  #어플리케이션 아이콘을 설정
#타이틀에 사용하는 이미지 파일은 보통 png (파이썬이나 어플리케이션과 궁합이 맞다.)
#jpg 는 고해상도를 압축한거라 icon이 안어울리고, gif 는 256 칼라뿐이다.
# 우선 그림파일을 QIcon 으로 아이콘화 시키고 , 그걸 윈도우 창에 사용한다는 setWindewIcon을 사용

#self.setGeometry(300,300,300,200)
# x좌표, y좌표, width값, height값
# 위치와 크기 전부를 설정할 수 있다.