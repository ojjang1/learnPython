# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:38:28 2020

@author: USER
"""


# Matplotlib 기본 사용
'''
Matplotlib 라이브러리를 이용해서 그래프를 그리는 일반적인 방법.
Matplotlib 는 방대한 라이브러리
이중 pyplot 를 알아보자.
'''

# Pyplot 소개
'''
matplotlib.pyplot 은
Matplotlib을 MATLAB 과 비슷하게 동작하도록 하는 명령어 스타일의 함수의 모음.

각각 pyplot 함수를 사용해서 그림 (figure)에 변화를 줄 수 있다.

예를 들어,
그림을 만들어서 플롯 영역을 만들고, 
몇개의 라인을 플롯하고,
라벨(label)들로 꾸미는 등의 일을 할 수 있다.

'''

# 기본 그래프
'''
pyplot으로 어떤 값들을 시각화 하는 것은 매우 간단.

pyplot.plot() 에 하나의 리스트를 입력함으로써 그래프가 그려진다.

matplotlib은
리스트의 값들이  y 값들이라고 가정하고,
x 값들 ([0, 1, 2, 3])  을 자동으로 만들어낸다.
'''

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('y-label')
plt.show()

# y 값만 넣어줬는데 자동으로 x값들을 생성해서 45도 각도의 선그래프를 만들어준다.


'''
plot()은 다재다능한 (versatile)한 명령어여서,
임의의 개수의 인자를 받을 수 있다.

예를 들어, 아래와 같이 입력하면, x와 y값을 그대프로 나타낼 수 있다.
'''
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

# axis() 를 이용해서 축의 [xmin, xmax, ymin, ymax] 범위를 지정.
plt.axis([0, 6, 0, 20])
plt.show()

# 스타일 지정하기
'''
x, y 값 인자에 대해
색상과 선의 형태를 지정하는 포맷 문자열을 세번쨰 인자에 입력할 수 있다.

디폴트 포멧 문자열은 'b-' 인데 파란색(blue)의 선 (line, '-')을 의미.

아래의 'ro' 는 빨간색(red) 의 원형 (circle, 'o') 마커를 의미.
'''

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')

# axis() 를 이용해서 축의 [xmin, xmax, ymin, ymax] 범위를 지정.
# 함수 안에 리스트 형태로 묶어서 넣어주면 된다.
plt.axis([0, 6, 0, 20])
plt.show()


# 여러 개의 그래프 그리기
'''
matplotlib 에서 리스트만 가지로 작업하는 것은 제한적이기 때문에,
일반적으로 Numpy 어레이를 이용.

사실, 모든 시퀀스는 내부적으로 Numpy 어레이로 변환된다.
'''

# 다양한 포멧 스타일의 여러 개의 라인을 하나의 그래프로 그리기.
import matplotlib.pyplot as plt
import numpy as np

# 200ms 간격으로 균일한 샘플된 시간
t = np.arange(0., 5., 0.2)

# 빨간 대쉬, 파란 사각형, 녹색 삼각형
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()




# Matplotlib 라벨 설정하기
''' 
xlabel(), ylabel() 함수를 사용해서
그래프의 x,y 축에 대한 라벨을 설정할 수 있다.
'''
import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16])

'''
xlabel()과 ylabel() 에 텍스트를 입력해주면,
각각의 축에 라벨이 나타난다.
'''

plt.xlabel('X-label')
plt.ylabel('Y-label')
plt.axis([0, 5, 0, 20])
plt.show()

'''
axis() 에 [x_min, x_max, y_min, y_max] 의 형태로
x,y 축의 범위를 지정.

입력 리스트는
꼭 네 개의 값 (x_min, x_max, y_min, y_max)  이 있어야 한다.

입력값이 없으면
데이터에 맞게 자동(Auto) 으로 범위를 지정.

'''

# Matplotlib 색깔 지정하기
# 자주 사용하는 색깔 외에도 다양한 색상을 지정할 수 있다.
import matplotlib.pyplot as plt
'''
plot() 에 color = 'springgreen' 과 같이 입력해주면,
springgreen 에 해당하는 색깔이 지정된다.
# 기존 칼러 이름으로 입력해도 되고
# 16 진수로도 입력 가능하다.
'''
plt.plot([1,2,3,4,],[1,4,9,16], color='springgreen')
plt.xlabel('X-label')
plt.ylabel('Y-label')
plt.axis([0, 5, 0, 20])
plt.show()


# Matplotlib 색깔 지정하기2
'''
16진수 코드(hex code)로도 색깔을 지정할 수 있다.
색깔, 마커와 선의 종류까지 모두 지정.
'''
import matplotlib.pyplot as plt
'''
색깔은 '#e35f62' 와 같이 16진수로, 마커는 circle,
선 종류는 대쉬(dashed) 로 지정.
'''
plt.plot([1,2,3,4,],[1,4,9,16], color='#e35f62' ,
         marker='o', linestyle = '--')
plt.xlabel('X-label')
plt.ylabel('Y-label')
plt.axis([0, 5, 0, 20])
plt.show()

