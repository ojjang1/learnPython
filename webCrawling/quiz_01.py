# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:14:08 2020

@author: USER
"""


## snack.db 를 읽어와서
## 문제 1 평균/ 최대/ 최소 / 4분위 값을 각각 구하시오

## db 접속하기

import sqlite3
import pandas as pd
import numpy as np

con = sqlite3.connect("C:/python/py_file/webCrawling/snack.db")

snack_df = pd.read_sql("SELECT * FROM snack", con)

print(snack_df)

snack_df.price.describe()

#평균
snack_mean = np.mean(snack_df.price)
print(snack_mean)

#최대
snack_max = max(snack_df.price)
print(snack_max)

#최소
snack_min = min(snack_df.price)
print(snack_min)


#1분위수
snack_1q = np.percentile(snack_df.price, 25) 
print(snack_1q)

#중앙값
snack_median = np.median(snack_df.price)
print(snack_median)

#3분위수
snack_3q = np.percentile(snack_df.price, 75)
print(snack_3q)



## 문제 2. 읽어들인 데이터를 Matplotlib 의 선형 차트로 출력하시오.
from matplotlib import pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

plt.plot(snack_df.title, snack_df.price)
plt.xlabel("title")
plt.xticks(rotation=90)

plt.bar(snack_df.title, snack_df.price)







