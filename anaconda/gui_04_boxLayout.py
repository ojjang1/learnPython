# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:23:45 2020

@author: USER
"""


# box 레이아웃
# 다양한 크기의 어플리케이션에서 사용할떄
# QHBoxLayout, QVBoxLayout   가로로 정렬하는 레이아웃 세로로 정렬하는 레이아웃
# 하나의 레이아웃박스에 다른 박스를 넣는 등 복합적으로 사용할 수 있다.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        okButton = QPushButton('OK')    #버튼 생성
        cancleButton = QPushButton("Cancel")    #버튼 생성
        
        hbox = QHBoxLayout()    #수평box레이아웃
        hbox.addStretch(1)     # 없으면 레이아웃에 균등배치 (있으면 레이아웃 양옆에 공간을 1:1 비율로 띄워준다.)
        hbox.addWidget(okButton)  #위젯은 레이아웃에 나타나게 하려면 add시켜야 한다.
        hbox.addWidget(cancleButton)
        hbox.addStretch(1)
        
        vbox = QVBoxLayout()   #수직box 레이아웃
        vbox.addStretch(3)   # 위와 아래의 공백을 3:1 비율로 해줘
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        self.setLayout(vbox)  # 전체를 갖고있는 레이아웃을 윈도우창에 보여달라고 set 한다.
        
        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 400, 200)
        self.show()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)   # 새창 만들려면 어플리케이션 객체 무조건 만들어줘야한다.
    ex = MyApp()
    sys.exit(app.exec_())  