# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:32:52 2020

@author: USER
"""


# 콤보박스 화살표로 나오는 html 에 select 태그 같은것

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.lbl = QLabel('Option',self)
        self.lbl.move(50,150)
        
        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50, 50)
        
        cb.activated[str].connect(self.onActivated)
        # 콤보스에 활성화 되어있는 str(글자)를 뽑아달라
        
        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
        # 크기를 변환시켜줘라.
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())