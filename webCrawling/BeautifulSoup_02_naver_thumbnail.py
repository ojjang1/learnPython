# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:53:54 2020

@author: USER
"""


# 네이버 웹툰 썸네일 가져오기

# 제목과 썸네일이 같이 존재하는 영역
from bs4 import BeautifulSoup
import requests

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

# 요일별 웹툰영역 추출하기
data1_list = soup.findAll('div',{'class':'col_inner'})
print(data1_list)


# 전체 웹툰 리스트
'''
요일별 웹툰영역중 제목과 썸네일 영역을 하나의 리스트로

썸네일과 제목이 들어간 부분이 <li> 태그로 묶여있는것을 확인
'''

li_list = []

for data1 in data1_list:
    # 제목+썸네일 영역 추출
    # 해당 부분을 차자 li_list와 병합
    li_list.extend(data1.findAll('li'))

print(li_list)    

## 각각의 요소중 <img> 태그의 제목과 썸네일(~.jpg)만 추출하기

for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    print(title, img_src)





















