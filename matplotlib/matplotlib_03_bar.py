# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:42:39 2020

@author: USER
"""


# Matplotlib 막대 그래프 그리기
'''
bar()함수를 이용해서 막대 그래프 (bar_graph)를 그릴 수 있다.
연도별 값을 갖는 데이터를 막대 그래프로 플롯.
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)

# years 는 x축에 표시될 연도이고, values 는 y 값.
years = ['2017', '2018', '2019']
values = [100, 400, 900]

# 먼저 bar() 함수에 x = ([0, 1, 2])와 값=([100,400,900]) 을 입력.
plt.bar(x, values)

'''
xticks() 에 x의 years 를 입력해주면,
x축에 '2017', '2018', '2019' 가 순서대로 표시된다.
'''

plt.xticks(x, years)

plt.show()


'''
막대 그래프에도
막대와 테두리의 색, 두께 등 다양한 스타일을 적용할 수 있다.

우선 bar() 함수에 x, y(=values) 값을 입력.
'''
plt.bar(x, values,
        width= 0.6,
        align= 'edge',
        color = 'springgreen',
        edgecolor = 'gray',
        linewidth = 3,
        tick_label = years,
        log=True)

plt.show()


'''
brth() 를 이용하면 수평막대 그래프를 그릴 수 있다.
'''
plt.barh(x, values,
        height= -0.6,
        align= 'edge',
        color = 'springgreen',
        edgecolor = 'gray',
        linewidth = 3,
        tick_label = years,
        log=False)

plt.show()


# https://matplotlib.org/index.html
# 라이브러리를 사용하는 방법은 직접 사이트에서 찾아보자.