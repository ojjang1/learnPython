# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:17:15 2020

@author: USER
"""


## Matplotlib 여러개의 곡선 그리기
# 세 개의 곡선을 하나의그래프에 그리기.

import matplotlib.pyplot as plt
import numpy as np

'''
Numpy를 사용해서 array 을 생성.
numpy.arange()
주어진 간격에 따라 균일한 array를 생성한다.
'''

a=np.arange(5)
b=np.arange(1,5)
c=np.arange(2,10,2)

print(a)  # [0 1 2 3 4] 0부터 입력값-1 까지
print(b)  # [1 2 3 4]  1부터 5-1까지 범위
print(c)  # [2 4 6 8]  2부터 10-1 까지 2 간격으로


'''
array a 는 [0. 0.2 0.4 0.6 0.8 1. 1.2 1.4 1.6 1.8]
'''
a = np.arange(0, 2, 0.2)


'''
plot() 에 x 값, y 값, 스타일을 순서대로 세 번씩 입력하면,
세 개의 곡선 (y=x, y=x^2, y=x^3)이 동시에 그려진다.
'''
plt.plot(a, a, 'r--',
         a, a**2, 'bo',
         a, a**3, 'g-.')

'''
'r-은' 빨간색(Red)의 대쉬(Dashed) 스타일 선,
'bo'는 파란색(Blue) 의 Circle 마커,
'g-.'은 녹색(Green)의 대쉬-닷(Dash-dot) 스타일 선을 의미.
'''
plt.show()



# 세 개의 곡선의 세세한 스타일을 설정할 수 있다.
import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0, 2, 0.2)

# 첫 번째 곡선의 스타일은 'bo'로,
plt.plot(a,a,'bo')

# 두 번째 곡선은 color = '#e35f62', marker='*', linewidth=2로,
plt.plot(a, a**2, color = '#e35f62', marker='*', linewidth=2)

# 세 번째 곡선은 color = 'springgreen', marker='^', markersize=9로
plt.plot(a, a**3, color = 'springgreen', marker='^', markersize=9)

plt.show()



# Matplotlib 그리드와 틱 설정하기
'''
gird() 와 tick_params() 를 이용해서
그래프의 그리드와 틱의 스타일을 설정할 수 있따.
'''
import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0, 2, 0.2)

plt.plot(a, a, 'bo')
plt.plot(a, a**2, color = '#e35f62', marker='*', linewidth=2)
plt.plot(a, a**3, color = 'springgreen', marker='^', markersize=9)

'''
그리드가 표시되도록 하려면
grid() 의 첫 번째 파라미터를 True로 설정.

axis = 'y' 로 설정하면 y 축의 그리드만 표시.

alpha 는 투명도를 설정합니다.
0으로 설정하면 투명하게,
1은 불투명하게 표시.

linestyle 을 대쉬(Dashed) 로 설정.
'''

plt.grid(True, axis='y', color='gray', alpha=0.5, linestyle = '--')



'''
tick_params() 를 이용해서 그래프의 틱(Tick)에 관련된 설정을 할 수 있다.

axis = 'both'로 설정하면 x, y 축의 틱에 모두 적용.

direction = 'in' 으로 틱의 방향을 그래프 안 쪽으로 설정.

틱의 길이(length)를 3 만큼으로 하고,
틱과 라벨의 거리(pad)를 6 만큼.
틱 라벨의 크기(labelsize)를 14 로 설정.
'''

plt.tick_params(axis='both', direction='in', length=3, pad=5, labelsize=14)

plt.show()


# Matplotlib 타이틀 설정하기
# title()을 이용해서 그래프의 제목 (타이틀)을 설정.

'''
plt.title()을 이용해서 그래프의 타이틀을 'Sample graph' 로 설정.
'''

plt.title('Sample graph')

plt.show()


# 2 - 위치와 오프셋
plt.title('Sample graph', loc='right', pad=20)

'''
loc='right' 로 설정하면,
타이틀이 그래프의 오른쪽 위에 나타나게 된다.

'left', 'center' , 'right' 로 설정할 수 있으며
디폴트는 'center'

pad = 20은
타이틀과 그래프와의 간격 (오프셋)을 포인트 단위로 설정
'''

# 3 - 폰트 설정
'''
fontdict 에 딕셔너리 형태로 폰트에 대한 설정을 입력할 수 있다.
'fontsize' 를 16으로, 'fontweight'를 'bold'로 설정.

'fontsize'는 포인트 단위의 숫자를 입력하거나,
'smaller', 'x-large' 등의 상대적인 설정을 할 수 있다.

'fontwight'에는 'normal', 'bold', 'heavy', 'light', 'ultrabold', 'ultralight'의
설정을 할 수 있다.
'''
title_font = {
    'fontsize' : 16,
    'fontweight' : 'bold'}

plt.title("Sample graph", fontdict=title_font, loc='left', pad=20)
