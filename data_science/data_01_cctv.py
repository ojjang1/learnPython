# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:55:18 2020

@author: USER
"""


'''
서울시 구별 CCTV 수를 파악하고,
인구대비 CCTV 비율을 파악해서 순위 비교

인구대비 CCTV의 평균치를 확인하고
그로부터 CCTV가 과하게 부족한 구를 확인

Python 기본문법/ Pandas와 Matplotlib의 기본적 사용법을 이용한 시각화
단순한 그래프 표현에서
한 단계 더 나아가 경향을 확인하고 시각화하는 기초 확인
'''

# CCTV 데이터와 인구 데이터 합치고 분석하기

# CCTV 데이터 읽기
import pandas as pd
import numpy as np

# CCTV 데이터와 인구 데이터 합치고 분석하기
CCTV_Seoul = pd.read_csv("01. CCTV_in_Seoul.csv", encoding = 'utf-8')
CCTV_Seoul.head()
type(CCTV_Seoul)

CCTV_Seoul.columns
type(CCTV_Seoul.columns)
# 오브젝트 형태로 반환인데
# 원래 리스트 로 반환하는데 데이터 프레임에서는 열이 시리즈 로 되어있다.
# 시리즈는 인덱스 영역과 벨류 영역으로 되어있어서
# 인덱스 로 값을 얻어 올 수 있다.
CCTV_Seoul.columns[0]

CCTV_Seoul.rename(columns = {CCTV_Seoul.columns[0]:'구별'}, inplace = True)
# rename함수는 pd 에 이는 모듈 컬렴명을 바꿔주는 함수는 없고, columns 의 글자를 바꿀 글자로만 바꿔주는것.
# inplace 는 바로 원본 데이터에 결과를 반영시키는 것
CCTV_Seoul.head()

# 인구 데이터 엙기 1
# 전체 데이터를 읽어 들이는 방식
pop_Seoul = pd.read_excel("01. population_in_Seoul.xls", encoding = 'utf-8')
pop_Seoul.head()
type(pop_Seoul)


# 인구 데이터 읽기 2 - 필요한 데이터만 선별하여 읽기
pop_Seoul = pd.read_excel("01. population_in_Seoul.xls",
                          header = 2,   # 엑셀파일의 2번째 줄부터 읽어줘라.
                          usecols = 'B, D, G, J, N',     # 엑셀파일의 컬럼명을 이용해서 필요한 컬럼만 선택                     
                          encoding = 'utf-8')
pop_Seoul.head()


# 알기 쉬운 컬럼명으로 변경
pop_Seoul.rename(columns = {pop_Seoul.columns[0] : '구별',
                            pop_Seoul.columns[1] : '인구수',
                            pop_Seoul.columns[2] : '한국인',
                            pop_Seoul.columns[3] : '외국인',
                            pop_Seoul.columns[4] : '고령자'}, inplace=True)


pop_Seoul.head()


# CCTV 데이터 파악하기
CCTV_Seoul.sort_values(by='소계', ascending=True).head(5)

CCTV_Seoul.sort_values(by='소계', ascending=False).head(5)
# 데이터프레임 모듈에 있는 정렬 시켜주는 함수 ,sort_values(by='기준열', ascending=정렬방식(T/F))
# 원본데이터는 수정안시키고 살펴보기위한 함수.

# 최근증가율 = (2016년+2015년,2014년)/2013년도 이전*100
CCTV_Seoul['최근증가율'] = (CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] + \
                            CCTV_Seoul['2014년']) / CCTV_Seoul['2013년도 이전'] * 100


CCTV_Seoul.sort_values(by='최근증가율', ascending=False).head(5)


# 서울시 인구 데이터 파악하기
pop_Seoul.head()

# 첫 번째 합게 행 삭제
pop_Seoul.drop([0], inplace = True)
pop_Seoul.head()
# unique() 는 중복값을 제거 해준다기 보다 unique 한것을 모아서 뽑아준다는 것
# 그래서 nan 값을 제거하고 사용하는것이 좋다.
 
   
# '구별' 컬럼의 중복값 제거
pop_Seoul['구별'].unique()


# '구별' 컬럼의 Null값 확인
pop_Seoul[pop_Seoul['구별'].isnull()]

# '구별' 컬럼의 NULL값 있는 행 제거
pop_Seoul.drop([26], inplace=True)
pop_Seoul.head(5)


''''
데이터분석 
1. 분석 데이터 수집 
    - 어떤 사이트의 데이터, 기사/문서, SNS 데이터 
2. 수집된 데이터 형식 확인 및 local 전처리
    - 1차로 프로그램 보다 직접 열어봐서 확인 1차 전처리 가능
3. 분석 Program에서 수집 데이터 읽기
    - R로 할거나 Python 으로 하느냐 선택하여 
    - 데이터 수집, 프로그램에서 데이터 읽을때
    - 인터넷에서 읽거나 pc 에서 저장한 후 읽는데
    - 보통 다운받을수 있는건 전부 받아서 분석하고
    - sns 같은 데이터 경우에는 프로그램에서 불러온 후
    - pc 에 저장 해야 한다.
    - 1차 전처리 넘어서 2차를 프로그램으로 가공하게 되면
    - 가공하는 중에서도 계속 저장하면서 해야한다.
    - 원본데이터, 1차가공데이터, 2차가공데이터 식으로
    - 쭉 구분해서 저장해야 한다.
4. 읽은 데이터 확인 및 2차 전처리 
'''

pop_Seoul['외국인비율'] = pop_Seoul['외국인']/ pop_Seoul['인구수']*100
pop_Seoul['고령자비율'] = pop_Seoul['고령자']/ pop_Seoul['인구수']*100
pop_Seoul.head()

pop_Seoul.sort_values(by='인구수', ascending=False).head(5)

# 각 컬럼 확인
pop_Seoul.sort_values(by='인구수', ascending=False).head(5)
pop_Seoul.sort_values(by='외국인', ascending=False).head(5)
pop_Seoul.sort_values(by='외국인비율', ascending=False).head(5)
pop_Seoul.sort_values(by='고령자', ascending=False).head(5)
pop_Seoul.sort_values(by='고령자비율', ascending=False).head(5)


##### CCTV 데이터와 인구 데이터 합치고 분석하기

# 두 개의 데이터 프레임을 합할 경우 동일 컬럼명은 하나('구별')로 통일 된다.
data_result = pd.merge(CCTV_Seoul, pop_Seoul, on='구별')
data_result.head()


# CCTV에 대한 '소계' 컬럼을 제외한 나머지 CCTV 데이터 삭제
del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
data_result.head()


# 시각화 작업을 위한 구이름('구별')을 index 화
data_result.set_index('구별', inplace = True)
data_result.head()

# CCTV 와 각 컬럼에 대한 상관관계 분석
# 상관관계 함수 : np.corrcoef()
np.corrcoef(data_result['고령자비율'], data_result['소계'])

np.corrcoef(data_result['외국인비율'], data_result['소계'])

np.corrcoef(data_result['인구수'], data_result['소계'])

data_result.sort_values(by='소계', ascending=False).head(5)

data_result.to_csv('data_result.csv')


# CCTV와 인구현황 그래프로 분석하기

import platform

# 폰트 설정 (특히 한글부분)
import  matplotlib.pyplot as plt
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':   #만약 운영체제가 맥이면
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows' :  #윈도우면
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
else :
    print('Unknown system... sorry~~~')
    

# CCTV 비율을 구하고 그에 따른 시각화 작업
data_result['CCTV비율'] = data_result['소계'] / data_result['인구수'] *100

data_result['CCTV비율'].sort_values().plot(kind='barh',
                                         grid = True,
                                         figsize=(10,10))
plt.show()

# 산점도 (인구수와 소계)
plt.figure(figsize = (6,6))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()


# 인구수와 CCTV는 상관계수가 양의 값이므로 산점도와 직선
# 직선 구하기 (Plotyfit을 이용한 회귀선)
# ployfit함수를 이용해서 예측 모델 z 의 계수를 생성
# 산점도의 회귀선을 구하기 위해 직선의 기울기를 구하기위한 계수
fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)
fp1

# 만들어진 예측 모델을 이용한 그래프 그리기
f1 = np.poly1d(fp1)  # y축 데이터
fx = np.linspace(100000, 700000, 100)  # x축 데이터

plt.figure(figsize=(10,10))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw = 3, color='g')
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()


# 조금 더 설득력 있는 자료 만들기
'''
직선이 전체 데이터의 대표값 역활을 한다면
인구수가 300,000 일 경우 CCTV는 1100 정도여야 한다는 결론
(직선과 만나는 부분)

가독성 향상을 위해 오차를 계산할 수 있는 코드 작성 후,
오타가 큰 순으로 데이터를 정렬
'''

fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)

f1 = np.poly1d(fp1)  # y축 데이터
fx = np.linspace(100000, 700000, 100)  # x축 데이터

data_result['오차'] = np.abs(data_result['소계'] - f1(data_result['인구수']))

df_sort = data_result.sort_values(by = '오차', ascending=False)
df_sort.head()


# plot 크기 설정
plt.figure(figsize=(14,10))

# 산점도
plt.scatter(data_result['인구수'], data_result['소계'],
            c = data_result['오차'], s = 50)

# 회귀선
plt.plot(fx, f1(fx), ls='dashed', lw = 3, color='g')

# 주요 10개 지역 구이름 출력
for n in range(10):
    plt.text(df_sort['인구수'][n] * 1.02, df_sort['소계'][n]*0.98,
             df_sort.index[n], fontsize = 15)

plt.xlabel('인구수')   #x 축 라벨
plt.ylabel('인구당비율') #y 축 라벨
plt.colorbar()          #오른쪽 색상 바
plt.grid()              # 가이드 라인
plt.show()


'''
분석
데이터를 분석 한다는 의미는
분석에 대한 결과가 있어야한다는 의미고
그 결과에 따라 결론이 나와야 한다.(결론 자체가 시각화가 아니다.)
시각화는 결론을 편하게 설명하기위한 방편에 불과하다.

그렇다면 이 결과를 위한 예측을 여러방법으로 해서 결론들을 내서
최종 결론을 내리는게 중요하다.
'''




