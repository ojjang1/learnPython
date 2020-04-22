# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:15:23 2020

@author: USER
"""


# Matplotlib 산점도 그리기
# scatter() 를 이용해서 산점도(scatter plot)를 그릴 수 있다.

import matplotlib.pyplot as plt
import numpy as np

'''
np.random.seed() 를 통해서 난수 생성의 시드를 설정하면,
같은 난수를 재사용 할 수 있다.

seed() 에 들어갈 파라미터는
0에서 4294967295 사이의 정수여야 한다.
'''

np.random.seed(19680801)

'''
x, y 의 위치, 마커의 색(color)과 면적(area)을 무작위로 지정.

예를 들어, x는
[0.7004545, .... , 0.14242124, 0.88585458] 같은
0에서 1사이의 무작위한 50개의 값을 갖는다.
'''

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2

'''
scatter() 에 x,y 위치를 입력.
s는 마커의 면적을,
c는 마커의 색을 지정.
alpha는 마커색의 투명도를 결정.
'''

plt.scatter(x,y, s=area, c=colors, alpha = 0.5)
plt.show()


# Matplotlib 3차원 산점도 그리기
'''
scatter() 를 이용해서 3차원 산점도 (3D Scatter plot)를 그리기.

3차원 그래프를 그리기 위해서
from mpl_toolkits.mplot3d import Axes3D 를 추가.

이 부분은 matplotlib 3.1.0  버전부터는
디폴트로 포함되기 때문에 적어주지 않아도 된다.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

n = 100
xmin, xmax, ymin, ymax, zmin, zmax = 0, 20, 0, 20, 0, 50
cmin, cmax = 0, 2

xs = (xmax - xmin) * np.random.rand(n) +xmin
ys = (xmax - xmin) * np.random.rand(n) +ymin
zs = (xmax - xmin) * np.random.rand(n) +zmin
color = (xmax - xmin) * np.random.rand(n) +cmin


# rcParams 를 이용해서 figure의 사이즈를 설정
plt.rcParams['figure.figsize'] = (6,6)
fig = plt.figure()
## 3차원 박스를 가로 세로 로 6등분 해서 쪼개는것

'''
3D axes 를 만들기 위해
add_subplot() 에 projection = '3d' 키워드를 입력
'''
ax = fig.add_subplot(111, projection = '3d')

'''
scatter() 함수에 x, y, z위치를 array의 형태로 입력
마커(marker)의 형태를 원형(circle)으로 설정
cmap = 'Greens'를 통해 colormap을 녹색 계열로 설정
'''

ax.scatter(xs, ys, zs, c=color, marker='o', s=15, cmap='Greens')

