# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:04:24 2020

@author: USER
"""

## 웹 크롤링 사용하기
'''
Beautifrlsoup - 파이썬 웹 크롤링 라이브러리

BeautifulSoup은 파이썬 웹 크롤링에 가장 널리 사용되는 라이브러리이자 툴 입니다.

웹 크롤링(Web crawling) 또는 스크래핑(Scrapping)은
웹 페이지들을 긁어와서 데이터를 추출하는 것을 말합니다.

웹 크롤러는 자동화된 방식으로 웹 페이지들을 탐색하는 컴퓨터 프로그램입니다.

파이썬과 BeautifulSoup 라이브러리를 이용하면
프로그래밍에 익숙하지 않은 비전공자나 입문자도 쉽게 크롤링을 할 수 있습니다.

BeautifulSoup 크롤링 예제에서 Requests와 BeautifulSoup 라이브러리를 사용하는데,
기본적으로 아나콘다 통합 패키지에 포함되어 있지만
설치되어 있지 않다면 설치를 진행합니다.

'''
# Requests 설치
# pip install requests
# 웹 서버로부터 데이터를 요청하기 위한 패키지

# BeautifulSoup 설치
# pip install beautifulsoup4
# html 데이터를 파싱하기 위한 패키지

# 네이버 날씨 미세먼지 가져오기

# 웹 페이지 가져오기
# https://search.naver.com/search.naver?query=날씨

from bs4 import BeautifulSoup as bs
import requests


html = requests.get('https://search.naver.com/search.naver?query=날씨')
# request.get 으로 서버에 요청
print(html.text)
# html 안에 있는 text 속성값들을 본다.
print(type(html))
# Response 타입
print(type(html.text))
# str 타입

## 그냥 str 타입에서 내가 원하는 정보를 뽑기 힘드니까 파싱한다.
## html태그로된 문자열을 beautifulSoup 로 전달해 객체로 만들어서 파싱
## xml,json 파일도 파싱 가능

# 파싱
soup = bs(html.text, 'html.parser')
# 두번째 인자는 어떤파일로 로 파싱할건지 설정해 주는것. xml,json 등등 다른것도 할 수 있다.
print(soup)


# 요소 1개 찾기(find)
# 미세먼지 정보가 있는 div 요소만 추출
data1 = soup.find('div',{"class":"detail_box"})
# div 태그 내부에 class 라는 속성명이 detail_box 라는 것 딱 하나반 찾아내달라.
print(data1)

# 요소 모두 찾기(findALL)
'''
find와 사용방법이 똑같으나
find 는 처음 매칭된 1개만
findALL 은 매칭된 모든 것을 '리스트'로 반환.
'''
data2 = data1.findAll('dd')
# data1 에서 태그명이 'dd' 라고 되어있는 것 모든것을 꺼내줘
# print(data2)
type(data2)


# 내부 텍스트 추출
# span태그에 속성과 속성값은 class = "num"

fine_dust = data2[0].find('span',{'class':"num"})
## 리스트 니까 [0] 으로 첫번째 요소만 꺼낼수 있고 거기서 검색
print(fine_dust)

# 내부 텍스트만 골라내도록 .text를 이용
fine_dust = data2[0].find('span',{'class':"num"}).text
print(fine_dust)



tet = data2[0].find('dd',{'class':"lv1"}).text
print(tet)

# 초 미세먼지 추출
'''
data2 변수에서
미세먼지는 0번 인덱스,
초미세먼지는 1번 인덱스,
오존농도는 2번 인덱스
'''

ultra_fine_dust = data2[1].find('span',{'class':'num'}).text
print(ultra_fine_dust)



# 오존 농도 추출
ozone = data2[2].find('span',{'class':'num'}).text
print(ozone)

from pandas import DataFrame

dust = DataFrame({"미세먼지":fine_dust,
                  "초미세먼지":ultra_fine_dust,
                  "오존농도":ozone},
                 index = ['2020.04.21'])

print(dust)
display(dust)
