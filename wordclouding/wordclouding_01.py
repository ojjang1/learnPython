# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:15:36 2020

@author: USER
"""

'''
# KoNLP 로 할 수 있는 것들
   문서 탐색하기
   연어(collocation) 찾기 (연관언어)
   구문 분석
   랜덤 텍스트 생성하기
   워드클라우드 그리기
   KoNLPy를 이용한 멀티쓰레딩 (java 라이브러리 기반이기때문에)
   말뭉치 탐색하기
'''
####### 자연어 처리 시작하기
'''
설치 목록 (설치 순서 반드시 지킬 것!!!!)
JDK (Java SE Downloads)
JAVA_HOME 설정
JPype 설치
KoNLPy 설치
Word Cloud 설치

JDK 설치 : Java JDK로 검색해서 OS에 맞춰 설치
JAVA_HOME 설정 :

JPype1 : conda install -c conda-forge jpype1
gensim install : pip install gensim
KoNLPy : pip install konlpy

WordCloud 설치 : pip install wordcloud

'''
'''
### JPype ###
Python 으로 하여금 거의 모든 Java 라이브러리를 사용하게 한다.
pip install JPype1-py3
conda install -c conda-forge jpype1
# R에서 Rjava 깔았던것처럼 자바로된 라이브러리를 사용하기위해설치

### gensim ###
text 데이터들의 topic modelling 하는 라이브러리. 
즉 topic modelling 에 대한 여러가지 기능이 구현되어 있다.

topic model (topic은 주제라는 뜻.)
예를 들면 
"트와이스는 너무 좋고 나는 모모를 좋아 한다. "  라는 문장이 있으면 
이 문장의 주제는 트와이스 혹은 모모 일것이다. 
그것은 관점에 따라 좀 다른데 
일반적으로 사람은 이 문장의 주제가 무엇일까? 라고 질문하면 
트와이스 라고 이야기 할 관점이 크고 
그다음에 "트와이스 멤버의 모모" 라고 이야기 하는사람도 있을 것이다.
이런식으로 텍스트 데이터 집단에서 해당 텍스트 집단들의 주제를 추출할수 있거나 
만들수 있는 모델을 topic modelling 이라고 할수 있다.

'''
##### 한글 자연어 처리 기초
# Kkma
from lib2to3.btm_utils import tokens
from konlpy.tag import Kkma
kkma = Kkma()

# Hannanum
from konlpy.tag import Hannanum
hannanum = Hannanum()

# Twitter
from konlpy.tag import Okt
t = Okt()


# 워드 클라우드
# WordCloud 설치 : pip install wordcloud

from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

# 워드 클라우드 폰트 설정
import matplotlib.pyplot as plt
import platform
path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc

#  문장의 유사도 측정
# Naive Bayes Classifier의 이해 - 영문
from nltk.tokenize import word_tokenize
import nltk