# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:24:43 2020

@author: USER
"""


# Radio 버튼
# RadioButton 여러개중에 하나만 선택된다.는 특징
# html 에서는 name속성을 같게 해줘야 하나만 선택되지만
# 파이썬에서는 자동으로 단일선택이다.

# text() 버튼의 텍스트를 반환
# setText() 라벨에 들어갈 텍스트를 설정
# setChecked() 버튼의 선택 여부를 설정
# isChecked() 버튼의 선택 여부를 반환

# 시그널
# 체크박스와 동일

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        rbtn1 = QRadioButton('First Button',self)
        rbtn1.move(50,50)
        rbtn1.setChecked(True)
        
        rbtn2 = QRadioButton(self)
        rbtn2.move(50,70)
        rbtn2.setText('Second Button')
        
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())