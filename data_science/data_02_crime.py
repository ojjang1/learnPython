# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:33:29 2020

@author: USER
"""


###################
# 강남 3구는 안전한가?
###################

'''
강남 3구의 주민들이 자신들이 거주하는 구의 체감 안전도를
높게 생각한다는 기사를 확인해 보도록 한다.
기사원문 http://news1.kr/articles/?1911504

Matplotlib의 heatmap 등을 그릴때
cmap 의 디폴트 설정이 변경되어 heatmap 등에서 cmap을 적용할 떄
옵션을 잡아주어야 동일한 효과가 나타난다.

Folium이 0.4.0으로 버전업 되면서
(R에서 지도 각내서 색상으로 표현해준것처럼)
choropleth 명령에서 get_str 옵션명이 geo_data 옵션명으로 변경됨.
circle marker 적용할때, fill=True 옵션을 반드시 사용해야 함.
'''

########
# 데이터 정리하기
# 필요한 모듈을 import

import numpy as np
import pandas as pd

'''
다운받은 데이터(csv) 파일을 읽는다.
콤마(,)로 천단위가 구분되어 있고, 한글 인코딩은 euc-kr
'''

crime_anal_police = pd.read_csv('02. crime_in_Seoul.csv', thousands= ',', encoding = 'euc-kr')
# 불러오면서 thousands 옵션으로 천단위로 묶인 ',' 를 제거해 줬다.
crime_anal_police.head()


'''
관서별로 되어 있는 데이터를 소속 구별로 변경
1. 경찰서 이름으로 구 정보 얻기
'''

## 구글 맵스를 사용해서 경찰서의 위치(위도, 경도) 정보를 받아온다.
# pip install googlemaps
import googlemaps

# 자신의 key를 이용
# gmaps_key = '구글맵 키'
gmaps = googlemaps.Client(key=gmaps_key)
r=gmaps.geocode('서울중부경찰서', language='ko')
print(r)
# JSON 형태로 반환 받아 오는것을 확인 할 수있따.
# 여기서 값을 꺼낼때 key 값을 통해 값을 꺼내오쟈.



# 중부서, 수서서 => 서울** 경찰서로 변경
station_name = []

for name in crime_anal_police['관서명']:
    station_name.append('서울' + str(name[:-1] +'경찰서'))
    
print(station_name)

# 경찰서 이름을 이용하여 주소 얻기
station_address = []
station_lat = []
station_lng = []

for name in station_name:
    tmp = gmaps.geocode(name, language = 'ko')
    station_address.append(tmp[0].get('formatted_address'))
    
    tmp_loc = tmp[0].get('geometry')
    
    station_lat.append(tmp_loc['location']['lat'])
    station_lng.append(tmp_loc['location']['lng'])
    
    print(name + '-->' + tmp[0].get('formatted_address'))
    

    
'''
저장한 주소를 띄어쓰기, 공백으로 나누고,
구별이라는 컬럼으로 저장.
'''
gu_name = []

for name in station_address:
    tmp = name.split()
    
    tmp_gu = [gu for gu in tmp if gu[-1] == '구'][0]
    gu_name.append(tmp_gu)
    
crime_anal_police['구별'] = gu_name
print(crime_anal_police.head())

'''
금천경찰서의 경우 관악구로 되어 있어서
금천구로 변경
'''

crime_anal_police[crime_anal_police['관서명']=='금천서']

crime_anal_police.loc[crime_anal_police['관서명']=='금천서', ['구별']] = '금천구'

#현재까지 작업 내용 저장.
crime_anal_police.to_csv('02_crime_in_Seoul_include_gu_name1.csv',sep = ',', encoding = 'utf-8')



##############
# 범죄 데이터 구별로 정리하기
from crime_in_seoul import station_lng, station_lat
import pandas as pd
import numpy as np

crime_anal_raw = pd.read_csv('02_crime_in_Seoul_include_gu_name1.csv', encoding = 'utf-8')

crime_anal_raw.head()

### pandas의 pivot_table

'''
pivot 테이블이란?
두 개의 열을 각각 행인덱스, 열인덱스로 사용하여 데이터를 조회하여 펼쳐 놓은 테이블 형태

원래의 데이터에서 내가 원하는 컬럼을 기준으로
다른컬럼을 재정리 해주기 위해 사용.

pd.pivot_table(df,                #피벗 테이블을 만들기 위한 기본 데이터
               index = [],        #pivot_table의 index를 설정(multi index도 가능)  
               columns = [],      # 원하는 columns을 설정
               values = [],       # column 에 해당하는 값
               aggfunc = [],      # 분석을 위한 파라미터 , 예) np.sum, np.mean 사용
               fillvalue = 0,     # Nan 값을 채우기
               margins = True)    # 모든 데이터의 결과를 아래에 붙일 것인가 설정
'''

# pivot_table을 이용
# 저장한 데이터를 관서별에서 구별로..
crime_anal = pd.pivot_table(crime_anal_raw, index = '구별', aggfunc = np.sum)
crime_anal.head()

print(crime_anal)


'''
각 범죄별 검거율을 계산하고,
검거 건수는 검거율로 대체한 후, 검거 건수는 삭제
'''
crime_anal['강간검거율'] = crime_anal['강간 검거']/crime_anal['강간 발생']*100
crime_anal['강도검거율'] = crime_anal['강도 검거']/crime_anal['강도 발생']*100
crime_anal['살인검거율'] = crime_anal['살인 검거']/crime_anal['살인 발생']*100
crime_anal['절도검거율'] = crime_anal['절도 검거']/crime_anal['절도 발생']*100
crime_anal['폭력검거율'] = crime_anal['폭력 검거']/crime_anal['폭력 발생']*100

del crime_anal['강간 검거']
del crime_anal['강도 검거']
del crime_anal['살인 검거']
del crime_anal['절도 검거']
del crime_anal['폭력 검거']

print(crime_anal.head())


'''
100 이 넘는 숫자들은 100으로 처리.
'''
con_list = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']

for column in con_list:
    crime_anal.loc[crime_anal[column] > 100, column] = 100
    
print(crime_anal.head())


# 컬럼 뒤에 발생이라는 단어 삭제 : rename()를 사용
crime_anal.rename(columns = {'강간 발생' : '강간',
                             '강도 발생' : '강도',
                             '살인 발생' : '살인',
                             '절도 발생' : '절도',
                             '폭력 발생' : '폭력'}, inplace = True)

print(crime_anal.head())


#############
# 데이터 표현을 위해 전처리
'''
강도와 살인은 두 자리수,
절도와 폭력은 네 자리수로 구성 되어 있어
각각을 비슷한 범위에 놓고 비교하는 것이 편리하기 때문에
각 컬럼별로 정규화(NORMALIZE) 작업...

각 항목의 최대값을 1로 두면,
추후 범죄발생 건수를 종합적으로 비교할 때 편리.

강간, 강도, 살인, 절도, 폭력에 대하여
각 컬럼별로 정규화(NORMALIZE)

파이썬의 머신러닝에 관한 모듈 중
scikit learn 에 있는 전처리(pregrocession) 도구에는
최소, 최대값을 이용하여 정규화시키는 함수가 존재 : MinMaxScaler()
'''

from sklearn import preprocessing

col = ['강간','강도','살인', '절도', '폭력']

x = crime_anal[col].values

min_max_scaler = preprocessing.MinMaxScaler()

x_scaled = min_max_scaler.fit_transform(x.astype(float))

crime_anal_norm = pd.DataFrame(x_scaled, columns = col, index = crime_anal.index)


# 정규화된 데이터프레임에 검거율 추가
col2 = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']

crime_anal_norm[col2] = crime_anal[col2]

print(crime_anal_norm.head())


# cctv_result.csv에서 구별 인구수와 CCTV 개수만 추가
result_CCTV = pd.read_csv('01. CCTV_result.csv', encoding = "UTF-8", index_col = '구별')

crime_anal_norm[['인구수','CCTV']] = result_CCTV[['인구수','소계']]

print('인구수와 CCTV 개수 =>', crime_anal_norm.head())


# 발생 건수의 합을 '범죄'라는 컬럼으로 합하여 추가

col = ['강간','강도','살인', '절도', '폭력']

crime_anal_norm['범죄'] = np.sum(crime_anal_norm[col],axis=1)

print('범죄라는 컬럼으로 합 => ', crime_anal_norm.head())


# 검거율도 통합하여 추가
col2 = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']

crime_anal_norm['검거'] =  np.sum(crime_anal_norm[col2], axis=1)

print('검거율도 통합 => ',crime_anal_norm.head())



import  matplotlib.pyplot as plt
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

import seaborn as sns  #다수의 상관관계 표현하기 위한 모듈
import platform        #한글 폰트 설정하기위한 모듈


if platform.system() == 'Darwin':   #만약 운영체제가 맥이면
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows' :  #윈도우면
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
else :
    print('Unknown system... sorry~~~')
    

# pariplot() 상관관계 : "강도, "살인", "폭력"

sns.pairplot(crime_anal_norm, vars=['강도','살인','폭력'], kind='reg', height=3)
plt.show()

'''
강도와 폭력, 살인과 폭력, 강도와 살인 모두 양의 상관관계를 보임
'''


# pairplot() 상관관계 : "인구수", "CCTV", "살인", "강도"
sns.pairplot(crime_anal_norm, x_vars=["인구수", "CCTV"], y_vars =["살인","강도"], kind='reg', size=3)
plt.show()

'''
전체적인 상관계수는 CCTV와 살인의 관계가 낮을지 몰라도
CCTV가 없을 때 살인 사건 많은 구간있음.
즉, CCTV수를 기준으로 좌측면에 살인과 강도의 높은 수를 갖는 데이터가 보임.
'''

# pairplot() 상관관계 : "인구수", "CCTV", "살인검거율","폭력검거율"
sns.pairplot(crime_anal_norm, x_vars=['인구수', 'CCTV'],
             y_vars=['살인검거율','폭력검거율'], kind='reg', size = 3)
plt.show()

'''
살인 및 폭력 검거율과 CCTV의 관계가 음의 상관계스도 보여줌
인구수와 살인 및 폭력 검거율도 음의 상관관계를 보임
'''

# pairplot() 상관관계 : '인구수', 'CCTV', '절도검거율', '강도검거율'

sns.pairplot(crime_anal_norm, x_vars=['인구수', 'CCTV'],
             y_vars = ['절도검거율', '강도검거율'], kind = 'reg', size=3)
plt.show()

'''
CCTV 와 강도 검거율은 확실한 음의 상관관계가 있음
'''


# 검거율의 합계인 검거 항목 최고 값을 100으로 한정한 후,
# 그 값으로 정렬
tmp_max = crime_anal_norm['검거'].max()

crime_anal_norm['검거'] = crime_anal_norm['검거'] / tmp_max *100

crime_anal_norm_sort = crime_anal_norm.sort_values(by = '검거', ascending = False)

crime_anal_norm_sort.head()




# heatmap 으로 시각화
target_col = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']

crime_anal_norm_sort = crime_anal_norm.sort_values(by = '검거', ascending = False)

plt.figure(figsize = (10,10))

sns.heatmap(crime_anal_norm_sort[target_col],
            annot = True, fmt = 'f',
            linewidths = .5,      #linewidth 는 칸 간격 의미.
            cmap= 'RdPu')

plt.title('범죄 검거 비율 (정규화된 검거의 합으로 정렬)')
plt.show()




# 발생 건수 정렬하여 heatmap 으로 시각화 
target_col = ['강간','강도','살인', '절도', '폭력', '범죄']

crime_anal_norm['범죄'] = crime_anal_norm['범죄'] /5

crime_anal_norm_sort = crime_anal_norm.sort_values(by = '범죄', ascending = False)

plt.figure(figsize = (10,10))

sns.heatmap(crime_anal_norm_sort[target_col],
            annot = True, fmt = 'f',
            linewidths = .5,      #linewidth 는 칸 간격 의미.
            cmap= 'RdPu')

plt.title('범죄 비율 (정규화된 발생 건수로 정렬)')
plt.show()

# 여기까지 작업 저장
crime_anal_norm.to_csv("02_crime_in_Seoul_final1.csv", sep= ',', encoding = "utf-8")
# UTF-8 요즘 인코딩의 표준이기때문에 해주면 좋다?


crime_anal_norm = pd.read_csv("02_crime_in_Seoul_final1.csv", encoding = "UTF-8")


################################
import json

geo_path = '02. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

crime_anal_raw['lat'] = station_lat
crime_anal_raw['lng'] = station_lng

col = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']
tmp = crime_anal_raw[col] / crime_anal_raw[col].max()

crime_anal_raw['검거'] = np.sum(tmp, axis=1)

crime_anal_raw.head()


############
import folium
# 지도 시각화 작업 모듈
import webbrowser
#  html 을 바로 실행시켜 주는 모듈
############
map = folium.Map(location = [37.5502, 126.982], zoom_start=11)
# 먼저 맵 객체를 생성 기분 위치를 지정해주고, 어느정도 확대할 것인지를 설정.

# 로드된 지도위에 각 경찰서 위치를 marking
for n in crime_anal_raw.index:
    folium.Marker([crime_anal_raw['lat'][n], crime_anal_raw['lng'][n]]).add_to(map)

# 저장.
map
map.save('folium_kr.html')
webbrowser.open_new("folium_kr.html")


################
# 지도를 이용한 시각화 작업을 위해 지도의 중심 좌표를 이용하여 12배 확대
map = folium.Map(location = [37.5502, 126.982], zoom_start=12)

# 로드된 지도 위에 각 경찰서의 검거율을 x10 배수의 크기(반지름)로 원을 그려준다.(외경 선과 내면 색 지정)
# .add_to()함수로 불러온 map 에 더해줌
for n in crime_anal_raw.index:
    folium.CircleMarker([crime_anal_raw['lat'][n], crime_anal_raw['lng'][n]],
                        radius = crime_anal_raw['검거'][n]*10,
                        color = '#3186cc',
                        fill_color = '#3186cc',
                        fill=True).add_to(map)

# map html파일로 저장 후 열기
map
map.save('folium_kr2.html')
webbrowser.open_new("folium_kr2.html")



################# 행정구역 별로 나누고 원 그림
##############
map = folium.Map(location = [37.5502, 126.982], zoom_start=12)

map.choropleth(geo_data=geo_str,
               data = crime_anal_norm['범죄'],
               columns = [crime_anal_norm.index, crime_anal_norm['범죄']],
               fill_color='PuRd',   #PuRd, YlGnBu
               key_on = 'feature.id')

for n in crime_anal_raw.index:
    folium.CircleMarker([crime_anal_raw['lat'][n], crime_anal_raw['lng'][n]],
                        radius = crime_anal_raw['검거'][n]*10,
                        color = '#3186cc',
                        fill_color = '#3186cc',
                        fill=True).add_to(map)

map.save('folium_kr3.html')
webbrowser.open_new("folium_kr3.html")


