# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:07:44 2020

@author: USER
"""

## QTextEdit
# 텍스트를 입력하면 단어의 갯수를 보여주는 gui를 만들어 보자.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout
# 엔터나 띄어쓰기를 하기위한 QTextEdit

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('Enter your sentence:')  #텍스트를 입력해 달라는 문장
        self.te = QTextEdit()     # 사용자에게 입력받기위한 모듈
        self.te.setAcceptRichText(False)
        self.lbl2 = QLabel('The number of words is 0') #텍스트를 입력하면 텍스트 수를 보여주는 라벨(처음값은 0으로 )

        self.te.textChanged.connect(self.text_changed)
        #텍스트에 변화가 일어나는 시그널이 생겨나면 함수 연결

        vbox = QVBoxLayout()         #라벨들 보여주기위한  레이아웃 추가.
        vbox.addWidget(self.lbl1)   #첫 라벨
        vbox.addWidget(self.te)     #입력창
        vbox.addWidget(self.lbl2)   #두번째 라벨
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QTextEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def text_changed(self):
        text = self.te.toPlainText()
        self.lbl2.setText('The number of words is ' + str(len(text.split())))
        # 텍스트가 변경되면 띄어쓰기 기준으로 쪼개서 길이를 합쳐보아요


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())