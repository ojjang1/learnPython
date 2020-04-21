# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:41:33 2020

@author: USER
"""


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(60, 40)
        
        qle = QLineEdit(self)
        qle.move(60,100)
        qle.textChanged[str].connect(self.onChanged)
        # 글자가 변했다고 시그널이오면 그 문자를 onChanged() 에 연결해 달리
        
        self.setWindowTitle('QLIneEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())