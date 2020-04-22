# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:29:39 2020

@author: USER
"""


# Matplotlib 히스토그램 그리기
# hist() 를 이용해서 히스토그램(histogram)을 그리기.

# 1- 값 입력하기
import matplotlib.pyplot as plt

'''
wieght 리스트는 몸무게 값을 나타냅니다.
'''
weight = [60, 81, 64, 56, 94, 61, 77, 66, 68, 59,
          71, 80, 59, 67, 81, 69, 73, 69, 74, 70, 65]

'''hist() 함수에 리스트의 형태로 값들을 직접 입력해주면 된다.'''
plt.hist(weight)


# 2 - 여러개의 히스토그램 그리기
import matplotlib.pyplot as plt
import numpy as np

'''
NumPy의 np.random.randn() 와
np.random.standard_normal(), np.random.rand() 함수를 이용해서
임의의 값들을 생성.
'''

# array a는 표준편차 2.0, 평균 1.0을 갖는 정규분포
a = 20. * np.random.randn(10000) + 1.0
# 연산을 하기위해 randn() 사용

# array b 는 표준정규분포를 따른다.
b = np.random.standard_normal(10000)
# randn() 과 같지만 튜플로 반환되니까 연산안할때 사용

# array c 는 -10.0에서 10.0 사이의 균일한 분포를 갖는 5000개의 임의의 값.
c = 20.0 * np.random.rand(5000) - 10.0


'''
세 개의 분포를 동시에 그래프에 나타내기.
plt.hist()

bins 는 몇 개의 영역으로 쪼갤지를 설정.

density = True 로 설정해 주면,
밀도함수가 되어서 막대의 아래 면적이 1이 된다.

alpha는 투명도를 의미합니다. 0.0에서 1.0 사이의 값을 갖는다.

histtype을 'step'으로 설정하면 막대 내부가 비어있고,
'stepfilled'로 설정하면 막대 내부가 채워진다.
'''

plt.hist(a, bins = 100, density = True, alpha = 0.7, histtype = 'step')
plt.hist(b, bins = 50, density = True, alpha = 0.5, histtype = 'stepfilled')
plt.hist(c, bins = 100, density = True, alpha = 0.9, histtype = 'step')

plt.show()



# 여러개 그래프 나타낼때 범례 주기

import matplotlib.pyplot as plt
import numpy as np

a = np.random.rand(1000)
b = np.random.rand(10000)
c = np.random.rand(100000)

plt.hist(a, bins = 100, density=True, alpha=0.5, histtype='step', label='n=1000')
plt.hist(b, bins = 100, density=True, alpha=0.75, histtype='step', label='n=10000')
plt.hist(c, bins = 100, density=True, alpha=1.0, histtype='step', label='n=100000')

plt.legend()


# 여러개 그래프 나타낼때 범례 주기

import matplotlib.pyplot as plt
import numpy as np

''' a는 [0, 10) 범위의 임의의 정수 1000개'''
a = np.random.randint(0, 10, 1000)

''' b는 [10, 20) 범위의 임의의 정수 1000개'''
b = np.random.randint(10, 20, 1000)

''' c는 [20, 30) 범위의 임의의 정수 1000개'''
c = np.random.randint(0, 20, 1000)

plt.hist(a, bins=100, density=False, alpha = 0.5, histtype='step', label = '0<=randint<10')
plt.hist(b, bins=100, density=False, alpha = 0.75, histtype='step', label = '10<=randint<20')
plt.hist(c, bins=100, density=False, alpha = 1.0, histtype='step', label = '0<=randint<20')

plt.legend()

plt.show()
