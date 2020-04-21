# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:14:55 2020

@author: USER
"""


##  QTextBrowser 클래스
# QTextEdit 의 확장형. 입력한 텍스트를 이용 할 수 이따.
# 읽기 전용이며 편집하려면 QTextEdit를 사용
# QTextEdit 의 setReadOnly() 를 사용해 편집이 불가능하게 해줌

import sys
from PyQt5.QtWidgets import (QApplication, QWidget
, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout)

# html 태그 포함한 입력값을 받기위한 라인 QLineEdit
# 텍스트를 해석해서 보여줄 다중창 QTextBrowser
# 텍스트를 전부 지워주기 위한 버튼 QPushButton
# 이 리벨들을 위에서부터 순서대로 나열하기 위한  QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le = QLineEdit()  #태그포함 한줄 입력 받기위한 매머드
        self.le.returnPressed.connect(self.append_text)
        # 엔터키를 눌렀을때(returnPressed) 함수 호출 및 값 자동 전달

        self.tb = QTextBrowser()  #html 해석할수 있는 객체 생성
        self.tb.setAcceptRichText(True)   #글자들을 접근 가능하게 서식있는 텍스트 (RichText) 를 사용
        self.tb.setOpenExternalLinks(True)  #링크를 눌렀을떄 외부와 연결되야 하기때문에 True

        self.clear_btn = QPushButton('Clear')     # 클릭했을때 목록을 다 지워주기 위한 버튼 생성
        self.clear_btn.pressed.connect(self.clear_text)
        # 버튼이 눌려지면 clear_text함수 호출

        vbox = QVBoxLayout()   # 한줄씩 차곡차곡 내려주기 위해 VBoxLayout 객체 생성
        vbox.addWidget(self.le, 0)  # addWidget만 쓰면 하나씩 차곡차곡 쌓이는데
        vbox.addWidget(self.tb, 1)  # 2번쨰 인자로 위치값을 수동으로 지정 해 줄 수 도 있다.
        vbox.addWidget(self.clear_btn, 2)  

        self.setLayout(vbox)

        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def append_text(self):      #한줄 입력을 하면 텍스트 브라우저에 보여주고 라인은 지운다.
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()         #.clear() 은 TestLine, TextBorwser, TextEdit 모두 있다.

    def clear_text(self):      #버튼 클릭했을때 텍스트 브라우저에있는 입력값 초기화
        self.tb.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())