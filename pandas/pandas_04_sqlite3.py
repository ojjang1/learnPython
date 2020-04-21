# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:28:38 2020

@author: USER
"""

## 경량 데이터 베이스 sqlite
## sqlite3 은 파이썬에서 경량 데이터베이스를 사용할수 있게 기능 제공해주는 모듈
## 암호화 해서 저장해놓기도 가능
## 확장자는 무조건 .db    오라클도 잘 보면 실제 저장되는 파일은 .db
## 그래서 .db로 저장행 다른 데이터베이스에서도 사용 할 수 있음.
## connect 는 폴어데 실제 파일을 저장하여 db에 연결시켜주는 함수.
## java 에서 db연결할때는 드라이버가 필요했는데 자바 로 구성된 패키지와 db를 연결하기 위함이고
## 이건 java와 관련이 없기 때문에 그냥 사용 가능
## connect 는 해당 파일이 자동으로 만들어지면 커넥션 객체를 만들어줌
## 그래서 우리는 이 커넥션 을 사용하여 db를 사용
## statement , prestatement 처럼 여기서는 cursor 객체를 만들면 여기서 db 쿼리 조작할수있게 된다.


## db 연결하기 3단계 - db연결하기위한 모듈 불러오기, 커넥션 객채 만들기, 쿼리쓰기위한 커서 객체 만들기.
import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

con = sqlite3.connect("C:/python\py_file/pandas/kospi.db")
print(type(con))

cursor = con.cursor()

## 컬럼명 Close로 쓰고십프나 db내장 변수 이름과 같기때문에 Closing 로 변환해서 사용
cursor.execute("CREATE TABLE kakao(Date text, Open int, High int, Low int, Closing int, Volumn int)")

cursor.execute("INSERT INTO kakao VALUES('16.06.03',97000, 98600, 96900, 98000, 321405)")

cursor.execute("SELECT * FROM kakao")
print(cursor.fetchone())
print(cursor.fetchone())
# 이것도 한줄 씩 읽어주는건가보다. fetchall() 이 전체를 불러오는것.
# select 하면 결과가 cursor 에 저장되고 그걸 fetchone() 로 한줄씩 읽어들인다. 이때 컬럼명은 제외하고 읽어낸다.


# 자동커밋 아니기때문에 커밋해줘야 한다.
con.commit()
#con.clost()

# 한꺼번에 읽어들이는 함수.
cursor.execute("SELECT * FROM kakao")
print(cursor.fetchall())


# 읽어들인 데이터를 활용하기
cursor.execute("SELECT * FROM kakao")
kakao = cursor.fetchall()
print(type(kakao))
print(kakao[0][0])
print(kakao[0][1])
print(kakao[0][2])
print(kakao[0][3])

con.commit()
con.close()
