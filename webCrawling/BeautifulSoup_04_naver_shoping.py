# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:38:25 2020

@author: USER
"""

### 네이버 쇼핑몰 best100 식품 카테고리에 스낵
# 썸네일 다운로드(이미지명은 이미지 제목) 및 db에 저장(이미지 제목 및 가격)


import errno
# 예외 처리할때 필요한 모듈 try/except
from bs4 import BeautifulSoup

import requests, re, os

from urllib.request import urlretrieve   #추가(다운로드)


# 저장 폴더를 생성
try:
    if not (os.path.isdir('snack')):
        os.makedirs(os.path.join('snack'))
        print("snack 폴더 생성 성공!")
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패!")
        exit()
        

# 웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("https://search.shopping.naver.com/best100v2/detail.nhn?catId=50001998")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()


# 이미지 영역 추출하기
data1_list = soup.findAll('li',{'class':'_itemSection'})
# print(data1_list)


# 전체 웹툰 리스트
li_list = []

for data1 in data1_list:
    #제목 + 썸네일 영역 추출
    li_list.extend(data1.findAll('div',{'class':'thumb_area'}))
    # 해당 부분을 찾아 li_list와 병합
# print(li_list)

# img = li_list[0].find('img')
# title = img['alt']
# img_src = img['data-original']


# 각각 썸네일과 제목 추출하기
for li in li_list:
    img = li.find('img')
    title = img['alt']
    img_src = img['data-original']
    #print(title, img_src)
    # 해당 영역의 글자가 아닌 것은 '' 로 치환시킨다.
    title = re.sub('[^0-9a-zA-Zㄱ-힗]','',title)
    #주소, 파일경로+파일명+확장자
    urlretrieve(img_src , './snack/'+title+'.jpg')
    

# db 에 저장하기위한 이름, 가격 리스트 뽑기
title_list = []
for li in li_list:
    img = li.find('img')
    title = img['alt']
    title_list.append(title)
    

# 가격을 리스트를 뽑기 위한 크롤링
div_list = []
for data1 in data1_list:
    div_list.extend(data1.findAll('div',{'class':'price'}))


# div_lsit 에서 가격 만 리스트에 저장
price_list = []
for num in div_list:
    price = num.find('span',{'class':'num'}).text
    price_list.append(re.sub(',','',price))
    

# print(price_list)
price = list(map(int,price_list))

# db 에 넣기위해 데이터프레임으로 만듬
import pandas as pd

df = pd.DataFrame({'title':title_list,
               'price':price})



## db 연결하기 3단계 - db연결하기위한 모듈 불러오기, 커넥션 객채 만들기, 쿼리쓰기위한 커서 객체 만들기.
import sqlite3

con = sqlite3.connect("C:/python/py_file/webCrawling/snack.db")

cursor = con.cursor()

## DataFrame은 DB에 저장할 수 있는 함수를 제공. : to_sql()
# Auto Commit이 기본
df.to_sql('snack',con,chunksize=1000, index = False)

# DataFrame은 DB를 통해 조회할 수 있는 쿼리도 제공
readed_df = pd.read_sql("SELECT * FROM snack", con)
print(readed_df)
help(df.to_sql)

con.close()
