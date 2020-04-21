# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:40:39 2020

@author: USER
"""


import sys
from PyQt5.QtWidgets import (QApplication, QWidget,QGridLayout, QLabel, QLineEdit, QTextEdit)

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)   #세팅코드를 맨 아래 써 도되고 초반에 써도된다.
        
        grid.addWidget(QLabel('Title:'),0,0)       #추가할 객채, 행번호, 열번호
        grid.addWidget(QLabel('Author:'),1,0)
        grid.addWidget(QLabel('Review:'),2,0)
        
        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QLineEdit(), 2, 1)
        
        self.setWindowTitle('QGridLayout')
        self.setGeometry(300,300,300,200)
        self.show()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)   # 새창 만들려면 어플리케이션 객체 무조건 만들어줘야한다.
    ex = MyApp()
    sys.exit(app.exec_())  