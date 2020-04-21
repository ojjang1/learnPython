# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:31:16 2020

@author: USER
"""


# QTabWidget
# 탭을 만들어 주는 위젯

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout
# QTabwidget 은 형태를 갖는 위젯
# 우리가 계속 상속받고 있는 QWidget 은 형태가 없는 위젯.

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        tab1 = QWidget()        # Q위젯 객체를 만든다.
        tab2 = QWidget()        # 이 곳에 다른 위젯들을 넣을어서 활용 할 수 있다.

        tabs = QTabWidget()    #탭 위젯 객체를 만들어준다.
        tabs.addTab(tab1, 'Tab1')  #위젯 안에 탭을 생성, Q위젯 탭이고, 탭이름 "Tab1" 이다.
        tabs.addTab(tab2, 'Tab2')

        
        vbox = QVBoxLayout()   
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())