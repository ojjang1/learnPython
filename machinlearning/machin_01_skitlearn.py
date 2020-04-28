# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 09:35:47 2020

@author: USER
"""


'''
Scikit-learn 
kmm - cnn - rnn

데이터 셋! 이란
기존 데이터 아닌 셋을 만들겟다 하면
학습데이터, - ex) 기존 수능 문제
훈련데이터, - ex) 모의 고사
예측데이터, - ex) 2020 수능 예측.(일반적으로 예측이 힘드니까 모의고사를 갖다 쓰고 있지.)
를 만들어야 한다.
그래서 모의고사를 예측데이터로 보내면
훈련 데이터가 없으니까 학습데이터를 가지고 학습데이터/ 훈련데이터로 구별한다. 비율은 모델에 따라 다름
학습데이터  - 문제 와 정답이 있어야 한다. 
이처럼 알려져있는 사례를 확용해 학습시키는것을 지도 학습이라고 함.

즉 , 학습위한 데이터를 위해  문제 와 답 을 매겨주는 라벨링 작업을 해야 한다.

만약 이미지를 가지고 학습을 하곘다.

데이터 셑 사이트를 이용하는 방법도 있다.
문제는 - 국내 용은 별로 없어요..

우리는 iris 데이터 셋을 사용.
붓꽃의 품종, 꽃입, 꽃받침, 폭과 길이를 담은 데이터 셋
'''

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
# 데이터셋 로드하는 함수.

iris = load_iris()
type(iris)
# sklearn.utils.Bunch
print(iris)

print(iris.keys())
# 데이터의 컬럼명 알아내는 함수.
#dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])
print(iris.target_names)
# 데이터의 특성중에 직접접속 함수(품종)
# ['setosa' 'versicolor' 'virginica']
print(iris.feature_names)
# 각 품종에 대한 내부 특서에 대한 이름을 알아보기
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# 꽃받침 너비와 길이, 꽃입 너비와 깊이


# feature 현제 데이터셋이 아닌 세로운 데이터 가 또 들어올 경우
# 그 데이터가 어떤 품종에 해당하는지 꽃바침의 길이와 너비, 꽃잎의 길이 너비를 이용해
# 품종을 판별하기 위한 머신러닝 모델을 만들기위한 구분점

# 농업쪽이나 화훼쪽 에도 이런 데이터가 있어서
# 이런 데이터셋 만드는것이 가능.

iris.data[:10]

'''
target  # 품종을 숫자로 나타냄.
tartget_names   품종 
feature
feature_names
'''
print(iris.target)
# 라벨링 한 결과라고 볼 수 있다.
# 지금 지도 학습을 하고 있는것을 잊지 말자. 문제와 답이 필요

# 머신러닝 모델 만들때! 이런 기존 데이터로 해보고..학습도 중요하지만 성능 평가도 중요
# 데이터도 중요하지만 모델 성능이 안좋으면 모델을 다시 만들어야 하기때문에
# 결코 한가지 생각으로만 만들기는 매우 어렵다.

# 모델의 성능을 평가하지 않으면
# "과적합(Overfitting)" 이 되었는지 '일반화' 되지 않았는지 판단 할 수 없다.
# 너무 과도한 학습을 시켜서 성능이 안좋아지는것이 "과적합(Overfitting)"
# 데이터를 전부 학습하는데 쓴다면 모델 정확도는 높아지지만 새로운 데이터에대해 예측도가 떨어지는
# 과적합 상태가 나타날 수 있다.

# 머신러닝의 목적은 성능(모델의 성능)을 높이고 일반화 하는 데에 있다.
# 1 학습데이터, 2, 테스트 데이터를 적절하게 나누어야 한다.

# scikit-learn 에는 데이터 셋을 분리 시켜주는 train_test_split 이란 함수가 제공된다.

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(iris.data,    # 데이터 셋
                                                    iris.target,  # 학습시킬 값 (우리는 품좀을 알아내려한다.)
                                                    test_size = 0.3,  # test_size 를 30% .. 7:3 비율로 
                                                    random_state = 2019) # 
# 총 4가지 값을 반환해줌. 변수명은 바꿔도 되나 받는값이 4개인거랑 순서는 잘 살펴봐야한다.
print(X_train)
print(X_test)
print(Y_train)
print(Y_test)


# 1. 주제 : 붓꼿의 품종을 학습시키곘다.
# 2. 사용 기기 : sklearn
# 3 학습데이터 테스트 데이터 분리
# 4. 이제 학습 시켜야한다(학습모델이 필요 KNN)

# KNN 모델을 사용해 학습을 시킬건데 fit 함수로 사용한다.

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train,Y_train)

## KNN 모델!
# 1. sklearn 에서 갖고있는  KNN 모델 클래스 임포트
# 2. 모델로 객체를 만듬(이떄 근접계수 값을 넣어줌)
# 3. fit 함수로 훈련데이터, 훈련 정답 데이터 넣어준다.
# 근접도에 따라 데이터를 분류시키는 모델이기 때문에
# 근접이 어떤게 필요한지 근접의 정도를 알려줘야 한다. 그 옵션이 n_neighbors = 3 이다.

# score 함수로 학습 평가를 test 데이터로 해서 성능을 평가
print('accoracy : {:.2f}'.format(knn.score(X_test, Y_test)))
# 100% 나오는 이유는 지금 아이리스 데이터가 품종이 순서대로 이루어져있기때문에
# 0,0,0,0,1,1,1,1,2,2,  이런식으로 학습했기 때문에.
# 다른 결과를 살펴보고 싶을떄 테스트데이터를 20,10% 로 하는 경우도 있다.


# 각 모델별로 임포트할것, 정리하고
# 모델 생성할떄 생성자쪽으로 무엇을 넘겨주는지 정리하고
# fit 으로 학습을 시키고
# score 로 평가를 하는 과정으로 정리해두자.


# 지금까지는 1차 학습방법

# 2차 교차 검증 학습방법
# k-폴드 방법
# 교차검증 하려면 데이터를 쪼개 주어야 한다.
# k- 겹 교차 검증에서
# k 는 5 or 10 과 같은 숫자가 들어가며
# 데이터를 비슷한 크기의 집합 K개 로 나눈다.
# 데이터를 5개 의 폴더로 나누고
# 각 폴드에서 5개로 분할해서 1번째는 테스트용, 나머지는 훈련용으로 사용
# 다름 폴드는 2번쨰를 테스트용, 나머지는 훈련용 이런식으로 사용

## 중요 = 각 겹마다 정확도를 알아내고 이 값들의 평균값을 내어서 성능을 평가.
# 교차검증을 위해 cross_val_score 함수를 불러온다.
# 아까 사용한 값보다 더 훈련을 잘 시킬 가능성이있다(물론 데이터를 뭘 넣느냐에따라)


## 검증
# 1 선형회귀
# 2. KNN
# 3. SVM
# 4. 의사결정틀
# 5. 랜덤 포레스트 모델
# 검증을 해보자. 


# 교차 검증
from sklearn.model_selection import cross_val_score

# 유방암
from sklearn.datasets import load_breast_cancer

#선형 회귀
from sklearn.linear_model import LinearRegression

# KNN
from sklearn.neighbors import KNeighborsClassifier

# SVN
from sklearn.svm import LinearSVC

# 의사 결정 트리
from sklearn.tree import DecisionTreeClassifier

# 랜덤 포레스트
from sklearn.ensemble import RandomForestClassifier

cancer = load_breast_cancer()
print(cancer)

print(cancer.keys())
# dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])
print(cancer.data)
print(cancer.target)
print(cancer.target_names)
print(cancer.feature_names)

# 1 선형 회기 모델
lr = LinearRegression()
# 선형회귀모델 객체 생성

# 2. KNN 학습모델
# 원래는 모델 만들기위해 4 라는 값을 쓰기위한 검증이 필요하다 원래는
# 이번에는 그냥 비교검증을 위해 미리 정해짐
knn = KNeighborsClassifier(n_neighbors = 4)


# 3. SVN
svm = LinearSVC(random_state = 0)


# 4. 의사결정트리 학습모델
tree = DecisionTreeClassifier(max_depth=3, random_state=0)

# 5. 랜덤포레스트 학습 모델
forest = RandomForestClassifier(n_estimators = 6)


# 선형회귀 학습 후 교차 검증
score1 = cross_val_score(lr, cancer.data, cancer.target)

# KNN 학습 후 , 교차 검증
score2 = cross_val_score(knn, cancer.data, cancer.target)

# SVM 학습 후, 교차 검증
score3 = cross_val_score(svm, cancer.data, cancer.target)

# 의사결정 트리 학습 후, 교차점증
score4 = cross_val_score(tree, cancer.data, cancer.target)

# 랜덤포레스트 학습 후 교차검증
score5 = cross_val_score(forest, cancer.data, cancer.target)

# 교차검증 함수는 1개다, 첫번째는 모델, 그다음 데이터 , 그다음 타겟데이터
# 스코어에 5개가 들어가서 각가에 대한 평균을 구해준다.
print('선형회귀 교차검증 점수 : {:.2f}'.format(score1.mean()))  # 0.70
print('KNN 교차검증 점수 : {:.2f}'.format(score2.mean()))       # 0.92
print('SVM 교차검증 점수 : {:.2f}'.format(score3.mean()))       # 0.82
print('의사결정트리 교차검증 점수 : {:.2f}'.format(score4.mean()))  #0.92
print('랜덤포레스트 교차검증 점수 : {:.2f}'.format(score5.mean()))  # 0.95


# 5개의 학습모델을 교차 검증 해본것이다.
# 다른 조건은 그대로 둔채 데이터 셋만 쪼개서 검증해보자

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(cancer.data,
                                                     cancer.target,
                                                     random_state=0)

# 각 모델들도 fit 함수를 가지고 있따.
# 각 모델에 학습시키기

lr = LinearRegression().fit(X_train, Y_train)

knn = KNeighborsClassifier(n_neighbors = 4).fit(X_train, Y_train)

svm = LinearSVC(random_state=4).fit(X_train, Y_train)

tree = DecisionTreeClassifier(max_depth = 3,
                              random_state = 0).fit(X_train, Y_train)

forest = RandomForestClassifier(n_estimators = 6).fit(X_train, Y_train)


## 학습시킨 데이터들 테스트 해보기
print('선형회귀 정확도 : {:.2f}'.format(lr.score(X_test, Y_test)))   #0.73
print('KNN 정확도 : {:.2f}'.format(knn.score(X_test, Y_test)))       #0.92
print('SVM 정확도 : {:.2f}'.format(svm.score(X_test, Y_test)))        #0.94
print('의사결정트리 정확도 : {:.2f}'.format(tree.score(X_test, Y_test)))   #0.94
print('랜덤포레스트 정확도 : {:.2f}'.format(forest.score(X_test, Y_test)))  #0.94


## 각각의 장단점
# 데이터를 쪼개게 되면 순서대로 데이터가 된 아까 붓꽃데이터 같은경우는 편향성있기 때문에
# 아까처럼 교차검증 방식으로 하면 데이터의 편향성을 줄일 수 있다.