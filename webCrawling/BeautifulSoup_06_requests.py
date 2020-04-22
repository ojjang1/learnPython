# -*- coding: utf-8 -*- r
"""
Created on Wed Apr 22 10:12:47 2020

@author: USER
"""


## Request 기본 사용

'''
html 소스 가져오기

Requests 를 사용하면 아래와 같이 간단한 코드만으로
웹페이지의 html 소스를 가져올 수 있다.
'''

import requests

# requests.get() 에 의한 response 에는 다양한 정보가 포함되어 있다.
r = requests.get('https://google.com')
html = r.text   # 유니코드 형태로 데이터를 꺼내오는것.
print(html)


'''
웹 펴이지의 content 를
유니코드 형태가 아니라 bytes 형태로 얻기 위해서는
r.text가 아닌 r.content를 사용할 수 도 있다.
'''
r = requests.get('https://google.com')
html = r.content  #bytes 형태로 데이터를 꺼내온다.
print(html)

# .text 나 .content 나 response 객체의 속성명이다 (함수가 아니다 주의)


# response 객체 : requests.get() 의 반환 객체
'''
response 객체는
HTTP request에 의한 서버의 응답 정보를 갖고 있따.
status_code, headers, encoding, ok 등의 속성을 이용하면
다양한 정보를 얻을 수 있다.
'''
import requests

r = requests.get('https://google.com')
html = r.content  #bytes 형태로 데이터를 꺼내온다.

print(r.status_code)
# 응답 결과 코드값. 웹에서 보내온 응답 값 404, 500 ,200
print(r.headers['Content-Type'])
# html 에서 meta 태그 의 속성 값을 꺼내온 것
print(r.encoding)
# 인코딩 방식
print(r.ok)
# 응답이 정상인지 문제가 발생됬는지 boolean 반환


'''
status_code는
정상일 경우 200,  페이지가 발견되지 않을 경우 404

encoding 방식은 ISO-8859-1 이고,
요청에 대한 응답이 정상적으로 이루어졌음을 알 수 있다.

ok 의 의미는
(status_code가 200보다 작거나 같은경우 True, 그렇지 않을경우 False)
'''

'''
만약 인코딩 방식이 달라서 한글이 제대로 표시되지 않으면
아래와 같이 인코딩 방식을 변경.
'''

r.encoding = 'utf-8'


'''
Request를 이용해서 html 소스를 가져왔지만.
단순한 문자열 형태이기 때문에 파싱(Parsing)에 적합하지 않다.

그렇기 때문에 BeautifulSoup를 이용해서
파이썬이 html 소스를 분석하고 데이터를 추출하기 편리하도록
객체로 반환
'''

# 인터넷상으로 데이터를 주고 받기 때문에
# 오늘 응답이 정상인지 확인하는 방법을 사용하여
# 응답이 제대로 됬는지, 예외처리를 해야하는지 를 알 수 있다.




