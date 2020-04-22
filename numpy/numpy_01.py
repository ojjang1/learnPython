# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:27:58 2020

@author: USER
"""


# NumPy 난수 생성 (Random 모듈)
# 난수 생성에 활용할 수 있는 NumPy의 random 모듈 (numpy.random)

# 1- random.rand() : 주어진 형태의 난수를 생성.
import numpy as np

# 예제1
'''
만들어진 난수 array는 주어진 값에 의해 결정되며,
[0,1) 범위에서 균일한 분포를 갖는다.
'''

a = np.random.rand(5)
print(a)
'''
결과 : [0.41401072 0.09536344 0.21888867 0.23587206 0.5897543 ]
실행할때 마다 결과가 달라짐
'''
b = np.random.rand(2,3)
print(b)
'''
결과 2행 3열짜리 리스트
[[0.7003673  0.74275081 0.70928001]
 [0.56674552 0.97778533 0.70633485]]

'''


'''
random.rand() 주어진 형태의 난수 array를 생성

random.randint() [최저값, 최대값) 의 범위에서 임의의 정수

random.randn() 표준 정규분포(standard normal distribution)를 갖는 난수를 반환

random.standard_normal() : randn()과  standard_normal()은 기능이 비슷하지만,
                            standard_normal()은 튜플을 인자로 받는다는 점에서 차이

random.random_sample() : [0.0, 1.0) 범위의 임의의 실수를 반환

random.choice() : 주어진 1차원 어레이에서 임의의 샘플을 생성

random.seed() : 난수 생성에 필요한 시드를 정한다.
                코드를 실행할 때마다 똑같은 난수가 생성
'''

