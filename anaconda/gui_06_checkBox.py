# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:05:32 2020

@author: USER
"""

# 체크박스 
# 선택되거나 해제될 떄 stateChanged() 상태변화 감지
# 체크되어있는지 확인하는 함수 isChecked()메서드 True,False로 반환
# setTristate() 메서드를 사용하여 변경없음 상태를 가질 수 있음
# checkState() 메서드는 정수 반환. 선택/변경없음/해제 2/1/0 값 반환
# toggle() 체크박스의 상태를 변겨
# text() 체크박스의 라벨 텍스트를 반환
# setText() 체크박스의 라벨 텍스트를 설정
# PyQt5 에서는 이벤트 라는것을 시그널이라고 표현.
# 시그널
# stateChanged() 체크박스의 상태가 바뀔때 신호를 발생
# pressed() 체크박스를 누를떄 신호를 발생
# released() 체크 박스에서 뗄 떄 신호를 발생
# clicked() 체크박스를 클릭할 때 신호를 발생

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox 
from PyQt5.QtCore import Qt
#checkState() 가 반환하는 상수를 갖는 애가 Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self)  # 첫번째는 라벨값, 두번째는 객체.
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())