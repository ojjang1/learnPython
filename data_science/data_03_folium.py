# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:32:47 2020

@author: USER
"""


import webbrowser
import pandas as pd
import folium

pop_Seoul = pd.read_excel("01. population_in_Seoul.xls",
                          header = 2,   # 엑셀파일의 2번째 줄부터 읽어줘라.
                          usecols = 'B,J',     # 엑셀파일의 컬럼명을 이용해서 필요한 컬럼만 선택                     
                          encoding = 'utf-8')

pop_Seoul.head()

pop_Seoul.rename(columns = {pop_Seoul.columns[0] : '구별',
                            pop_Seoul.columns[1] : '외국인'}, inplace=True)
pop_Seoul.구별
pop_Seoul.head()
pop_Seoul.describe()
pop_Seoul.info()
pop_Seoul.dropna(inplace = True)

import json

geo_path = '02. skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

map = folium.Map(location = [37.5502, 126.982], zoom_start=12)

map.choropleth(geo_data=geo_str,
               data = pop_Seoul['외국인'],
               columns = [pop_Seoul['구별'], pop_Seoul['외국인']],
               fill_color='PuRd',   #PuRd, YlGnBu
               key_on = 'feature.id')

map
map.save('folium_kr3.html')
webbrowser.open_new("folium_kr3.html")




#########################################
pop_korea = pd.read_csv("Total_People_2018.csv")
pop_korea.info()


geo_path1 = 'TL_SCCO_SIG_WGS84.json'
geo_str1 = json.load(open(geo_path1))

map1 = folium.Map(location = [37.5502, 126.982], zoom_start=9)

map1.choropleth(geo_data=geo_str1,
                data = pop_korea,
                columns = ['Code', "Population"],
                fill_color='PuRd',
                key_on = 'feature.properties.SIG_CD')

map1
map1.save('folium_kr4.html')
webbrowser.open_new("folium_kr4.html")
