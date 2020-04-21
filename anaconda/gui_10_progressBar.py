# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:07:08 2020

@author: USER
"""


# QProgressBar
# 수평, 수직의 진행 표시줄을 제공

# setMinimum(), setMaximun() 진행표시줄 최대,최소값 설정 
# 둘다 0으로 하면 무한 반복(주로 인터넷을 통해 파일 받을때 사용하는 방식)
# setRange() 한번에 범위를 설정

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer


class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.pbar = QProgressBar(self)   #프로그레스 객체 생성
        self.pbar.setGeometry(30, 40, 200, 25)  # 프로그래스 위치 , 크기 지정
        
        self.btn = QPushButton('Start', self)   #스타트버튼으로 시작되게 하기
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)
        
        self.timer = QBasicTimer()   # 시간에 따라 점점 늘어나게 하기위해 타이머 객체 생성
        self.step = 0   # 1씩 증가할것. 기본값은 0
        
        
        
        self.setWindowTitle('QProgerssBar')
        self.setGeometry(300,300,300,200)
        self.show()
        
    # 모든  Q위젯클래스들은 Q오브젝트를 상속받아 사용하는데
    # 그 내부에도 타이머 함수가 있어서 상속받은 함수를 오버라이드 한다. 
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()   #타이머를 멈춤
            self.btn.setText('Finished')
            return
        
        self.step = self.step +1
        self.pbar.setValue(self.step)   #프로그래스의 녹색 바 위치(크기) 지정
        
    # 위에 함수는 있는 함수 재정의 아래 함수는 사용자 함수
    def doAction(self):
        if self.timer.isActive():   #timer 가 start인지 stop 인지 boolean 값으로 반환
             self.timer.stop()     # stop는 그자리에서 멈추니까 옵션값없다.
             self.btn.setText('Start')
        else:
            self.timer.start(100,self)   #start()는 입력값은 종료값
            self.btn.setText('Stop')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())