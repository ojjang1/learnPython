# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 10:43:55 2020

@author: USER
"""


# 많이 본 네이버 뉴스

'''
파이썬과 BeautifulSoup을 이용하면
이 웹 크롤러를 간단하게 만들 수 있다.
네이버 뉴스의 '많이 본 뉴스'를 가져오기.
'''

import requests
# 웹 에서 데이터 요청하는 모듈
from bs4 import BeautifulSoup
# 데이터를 파싱하기위한 모듈

'''
주소 :
    https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&date=20200421
    
위의 주소에서 알 수 있듯이 맨 뒤에 날짜를 바꿔주면
해당하는 날짜의 많이 본 뉴스를 볼 수 있다.
'''

url = "https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&date=20200421"

r = requests.get(url)
html = r.content
soup = BeautifulSoup(html, 'html.parser')


# 원하는 데이터 추출하기
# 네이버 많이 본 뉴스 페이지에서 헤드라인만 추출해서 출력
titles_html = soup.select('.ranking_section > ol > li > dl > dt > a')
# 원하는 태그의 내부의 내부의 내부 태그를 찾아가는 방법 해당되는 태그 전부 가져온다.


# 30 개의 헤드라인이 순서대로 출력
for i in range(len(titles_html)):
    print(i+1, titles_html[i].text)
    # title_html 의 길이만큼 리스트를 반들어서 그 수만큼 반복.