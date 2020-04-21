# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:14:04 2020

@author: USER
"""


## QSplitter

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtCore import Qt
#QFrame - 구분선 만들어주는 애
#QSplitter - 구분선 만들어준것을 이용하는 애

class MyApp(QWidget):
    
     def __init__(self):
        super().__init__()
        self.initUI()
        
     def initUI(self):
        hbox = QHBoxLayout()

        top = QFrame()
        top.setFrameShape(QFrame.Box)

        midleft = QFrame()
        midleft.setFrameShape(QFrame.StyledPanel)

        midright = QFrame()
        midright.setFrameShape(QFrame.Panel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Sunken)

        splitter1 = QSplitter(Qt.Horizontal)  # 들어가는 상수는 쪼개지는 방향성(가로쪼개라(그럼 세로줄 나오겠지))
        splitter1.addWidget(midleft)
        splitter1.addWidget(midright)

        splitter2 = QSplitter(Qt.Vertical)  # 세로로 쪼개라(그럼 가로로 나뉘겠지)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
        
        
        
        
        