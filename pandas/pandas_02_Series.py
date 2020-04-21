# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:07:02 2020

@author: USER
"""


##### Series 기초
'''
Pandas 의 series는 1차원 배열과 같은 자료 구조.
파이썬 리스트와 튜플도 1차원 배열과 같은 자료구조

사실 Pandas의 Series는
어떤 면에서는 파이썬의 리스타와 비슷하고
어떤 면에서는 파이썬의 딕셔너리와 닮은 자료구조
'''

'''
Series를 사용하기에 앞서
Pandas라는 모듈에서 직접 Series와 DataFrame을
로컬 네임스페이스로 import
(즉 판다스를 통쨰로 불러왔기 때문에 pandas 를 붙여 pandas.Series 라고 사용)
'''

import pandas
print(pandas.Series)

'''
Series를 직접 로컬 네임스페이스로 import 한 경우에는
pandas는 생략하고 바로 Series라고만 적으면 된다.
'''
from pandas import Series, DataFrame

kakao = Series([92600, 92400, 92100, 94300, 92300])
# list 를 Series클래스에 생성자에 전달하여 Series 객체를 만든것
print(kakao)
type(kakao)

# 실제로는 Series 는 리스트 형태지만 인덱스 번호까지 저장하여 일종에 인덱스번호:값 의 딕셔너리 형태로 저장된다.

'''
Series 객체는 
일차원 배열과 달리 값뿐만 아니라
각 값에 연결된 인덱스 값도 동시에 저장.

Series 객체 생성 시에
인덱스값을 따로 지정하지 않으면
기본적으로 Series 객체는 0부터 시작하는 정숫값을 사용하여 인덱싱.
# 번호 외에도 다른 인덱스를 부여할수 있다는게 특징
'''

print(kakao[0])
print(kakao[2])
print(kakao[4])


kakao2 = Series([92600, 92400, 92100, 94300, 92300],
                index=['2016-02-19','2016-02-18',
                       '2016-02-17','2016-02-16','2016-02-15'])
print(kakao2)

'''
kaka2라는 Series 객체는
인덱스값으로 날짜에 해당하는 문자열을 지정했기 때문에
정숫값으로 인덱싱하는 것 대신 날짜를 의미하는 문자열을 사용하여
각 날짜에 대한 증가를 바로 얻어올 수 있다.

'''

print(kakao2['2016-02-19'])
print(kakao2['2016-02-18'])
print(kakao2[0])        

'''
Series 객체의
index와 values 라는 이름의 속성을 통해 접근할 수 있다.
'''
for date in kakao2.index:
    print(date)
for ending_price in kakao2.values:
    print(ending_price)


## 인덱스 순서가 다른 시리즈끼리 연산이 가능할까?
'''
Pandas 의 Series는
서로 다르게 인덱싱 된 데이터에 대해서도 
알아서 덧셈 연산을 처리해 준다.
'''

# From pandas import Series, DataFrame

mine = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([40, 50, 60], index=['kt','naver','sk'])

merge = mine + friend
print(merge)
# 인덱스가 다르면 같은 인덱스끼리는 더하고
# 다른 인덱스는 NaN 값으로 변환된다.
# 값 + NaN 값은 NaN으로 처리 하는 듯
# 더하기, 뺴가, 곱하기, 나누기, 나머지, 몫 다됨.
























