# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 10:11:30 2020

@author: USER
"""


### BeautifulSoup 기본 사용

# 예제로 사용할 html 문서
# 카페의 (beautifulSoup 기본 사용 데이터) 게시글 내용 복사

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


# html 을 그냥 request 를 사용해서 불러오면 알아보기 힘드니까 간단하게 구조화 시켜주는 함수가 있따.

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# soup.prettify() : html 문서의 계층 구조를 알기 쉽게 보여준다.
print(soup.prettify())
# 콘솔창에서 예쁘게 정돈되서 확인할수 있는걸 알 수 있다.


# title 태그를 반환.
soup.title
print(soup.title)
# 결과 : <title>The Dormouse's story</title>

#title 태그의 이름('title')을 반환
soup.title.name
print(soup.title.name)
# 결과 : title

# title 태그의 문자열을 반환.
soup.title.string
print(soup.title.string)
# 결과 : The Dormouse's story

# title 태그의 부모 태그의 이름을 반환
soup.title.parent.name
print(soup.title.parent.name)
# 결과 : head


# 첫 p 태그를 반환.
soup.p
print(soup.p)
# 결과 : <p class="title"><b>The Dormouse's story</b></p>

# 'class' 속성이 있는 첫 p 태그를 반환.
# soup.p['class']
print(soup.p['class'])
# 결과 ['title']


# a 태그를 반환.
soup.a
print(soup.a)
# 결과 : <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>


# 모든 a 태그를 리스트 형태로 반환.
soup.find_all()
print(soup.find_all('a'))
# 결과 : 리스트로 반환받는다.를 잘 확인
'''
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
'''


# soup.find() : 설정한 값에 해당하는 태그를 반환.
# id가 'link3'인 태그를 반환.
soup.find(id='link3')
print(soup.find(id='link3'))
# 결과 :<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


# get() : href 속성을 반환
for link in soup.find_all('a'):
    print(link.get('href'))
# 결과: 
'''
http://example.com/elsie
http://example.com/lacie
http://example.com/tillie
'''


# get_text() : html 문서 안에 있는 텍스트를 반환.
print(soup.get_text())
# 결과 태그들은 나오지 않고 text 들만 나온다.


