# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:31:06 2020

@author: USER
"""


# ## 1. 붓꽃의 품종 분류
#  (1) 데이터 적재
# = scikit-learn  dataset 모듈에 포함되어 있다.

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
iris_dataset = load_iris()


print('iris_dataset의 키 : \n{}'.format(iris_dataset.keys()))

print(iris_dataset.DESCR)

print(iris_dataset['DESCR'][:200] + '\n...')  #데이터 셋 설명 앞부분만

# 항상 데이터셋에 대한 특성들을 확인 해야 한다.

# - 예측하려는 붓꽃 품종의 이름을 가지고 있는 key : target_names
format('타깃의 이름 :{}'.format(iris_dataset['target_names']))

# - 특성을 설명하는 문자열 리스트 : feature_names
format('특성의 이름 :{}'.format(iris_dataset['feature_names']))

# - 실제 데이터(target, data_) 중 data는
# 꽃잎의 길이와 폭, 꽃받침의 길이와 폭을 수치 값으로 가지고 있는 Numpy 배열
format('data의 타입 :{}'.format(type(iris_dataset['data'])))

format('data의 크기 :{}'.format(iris_dataset['data'].shape))

# - 이 배열은 150개 의 붗꽃 데이터를 가지고 있으며,
#   각 붓꽃마다 4개의 측정치를 가지고 있음.

# - 머신러닝에서 각 아이템은 샘플이라 하고 속성은 특성이라고 부름.
# - 그러므로 data 배열의 크기는 150 * 4 가 됨
# - 이는 scikit-learn 의 스타일이며 항상 데이터가 이런 구조일 거라 가정하고 있음

print('data의 처음 다섯 행: \n{}'.format(iris_dataset['data'][:5]))
# - 1열 : 꽃받침의 길이
# - 2열 : 꽃받침의 폭
# - 3열 : 꽃입의 길이
# - 4열 : 꽃입의 폭

# target 의 배열 : 샘플 붓꽃의 품종을 담은 Numpy 배열
print('data의 타입 : {}'.format(type(iris_dataset['target'])))
# data의 타입 : <class 'numpy.ndarray'>

print('data의 타입:{}'.format(iris_dataset['target'].shape))
# data의 타입:(150,)

print('타깃:\n {}'.format(iris_dataset['target']))
# 0: setosa, 1:1 versicolors, 2: virginica

# 항상 데이터를 분석해야 한다.   
# 진짜 중요함 어떤 데이터인지 어떤 형식인지 어떻게 결과과나올지
# 이걸 알아야 머신런닝이든 웹페이지 코딩이든 항상 해야한다.
# 그리고 이 데이터가 내부에서 도는 데이터인지 흐름, 외부에서 들어오는 데이터 인지 흐름
# 흐름을 파학하고 어떻게 데이터를 이동시킬지를 먼저 생각하고
# 이후에 공통적은 작엄은 모듈화, 
# 공통적은 분야는  Spring AOP 공통 관심사. 로 묶어서 처리.. 하는 일련의 과정을 열심히 해보자.


# ### (2) 훈련데이터와 테스트 데이터
# - 머신러닝 모델을 만들 떄 사용하는 훈련용 데이터와 모델이 얼마나 잘
#   작동하는지 측정하는 테스트 데이터를 나눈다.

# - skicit-learn은 데이터 셋을 섞어서 나눠주는 train_test_split 함수 제공
# - (훈련세투 : 75%, 테스트세트 : 25%)

# - scikit-learn 에서 데이터는 대문자 X로 표시하고 레이블은 소문자 y로 표기한다.
# - 이는 수학에서 함수의 입력을 x, 출력을 y로 나타내는 
# 표준공식 f(x) = y 에서 유래된 것이다.

# - 수학의 표기 방식을 따르되 데이터는 2차원 배열(행렬)이므로 대문자 X를,
#  타깃은 1차원 배열(벡트)이므로 소문자 y를 사용

from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'],
                                                    iris_dataset['target'],
                                                    random_state = 0)

# - train 데이터와, test 데이터로 나누기 전에 무작위로 섞어주지 않으면
#  순서대로 나누어 지기 때문에 y_test(테스트레이블) 값이 모두 2가 나오게 된다.

# - 세 클래스(품종) 중 하나만 포함한 테스트 세트를 사용하면
#  모델이 얼마나 잘 일반화 되었는지 알 수 없다.

# - 테스트 세트는 모든 클래스의 데이터를 포함하도록 잘 섞어야 한다.
# - random_state = 0 은 이 함수를 여러번 실행해도 같은 랜덤값이 리턴된다.

print("X_train 크기 : {}".format(X_train.shape))  #(112, 4)
print("y_train 크기 : {}".format(y_train.shape))  # (112,)

print("X_test 크기 : {}".format(X_test.shape))    #(38, 4)
print("y_test 크기 : {}".format(y_test.shape))    #(38,)



# 데이터 스케일링 작업 데이터 전처리
# ### (3) 데이터 살펴보기
# - 머신러닝 모델을 만들기 전에 모신러닝 없이도 풀 수 있는 문제가 아닌지,
#   혹은 필요한 정보가 누락되어 있는지 데이터를 조사해 보는 것이 좋다.

# - 실제 데이터에는 일관성이 없거나 이상한 값이 들어가 있는 경우가 종종 있다.


# ** 산점도 행렬을 통해 데이터의 특성을 찾아보다 **
# - 산점도 : 여러 변수로 이루어진 자료에서 
#   두 변수끼리 짝을 지어 작성된 산점도를 행렬 형태로 배열

# X_train 데이터를 사용해서 데이터 프레임을 만든다
iris_dataframe = pd.DataFrame(X_train,
                              columns = iris_dataset.feature_names)

iris_dataframe.head()

pd.plotting.scatter_matrix(iris_dataframe, c=y_train,
                           figsize = (15,15),
                           marker = 'o', hist_kwds = {'bins' : 20},
                           s = 60, alpha = .8)

# - 세 클래스가 꽃잎과 꽃받침의 측정값에 따라
#  비교적 잘 구분되어 있는 것을 볼 수 있다.
# - 클래스 구분을 위한 머신러닝 기법을 사용하면 잘 구분 될 것이다.


### (4) K- 최근접 이웃(K-nearest neiighbors, k-nn) 알고리즘을 이용한 머신러닝

# - 훈련데이터를 통해 모델이 만들어지고
#  새로운 데이터가 들어오면 가까운 훈련 데이터 포인트를 찾아 분류한다.

# - scikit-learn 의 모든 머신러닝 모델은
#  Estimator라는 파이썬 클래스로 각각 구현되어 있따.

# - k-최근접 이웃 분류 알고르즘은
#  neighbors 모듈 아래 KNeighborsClassifier 클래스에 구현되어 있다.

# - 모델을 사용하기 위해 클래스로부터 객체를 만들고 paramiter를 설정한다.
#  가장 중요한 이웃의 개수를 1로 지정하고 모델을 만들어 보자.

# 내부 알고리즘에 따라
# 새로운데이터가 들어오면 새로운 KNN 객체가 만들어지고 훈련데이터중에서
# 가장 가까운 값을 찾아 간다.


from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)


# - 훈련 데이터 셋으로 부터 모델을 만들기 위해 fit 메서드 사용

knn.fit(X_train, y_train)

# - fit 메서드는 knn 객체 자체를 변환시키면서 반환 시킨다.
# KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
#                     metric_params=None, n_jobs=None, n_neighbors=1, p=2,
#                     weights='uniform')


# ### (5) 예측하기
# - 위에서 만든 모델을 사용해서 새 데이터에 대한 예측을 만들 수 있다.

# - 야생에서 꽃받침의 길이는 3cm, 혹은 4.2cm
#   꽃잎의 길이는 0.8cm, 폭은 0.4cm인 붓꽃을 찾았다고 가정하고
#   이 붓꽃의 품종을 찾아보자


# - 측정값은 mumpy 배열로 만드는데,
#   하나의 붓꽃 샘플(10) 에 4가지 특성(4)이 있으므로 1 by 4배열을 만들어야 한다.

# - 붓꽃 하나에 측정값은 2차원 mumpy 배열에 행으로 들어가므로,
#   scikit-learn 은 항상 데이터가 2차원 배열일 것으로 예상
 
X_new = np.array([[3, 4.2, 0.8, 0.4]])
X_new

print('X_new.shape : {}'.format(X_new.shape))

prediction = knn.predict(X_new)
# knn 모델에 훈련데이터 가반 학습된 모델로 예측 해주는 함수.
print("예측 : {}".format(prediction))  # [0]


print('예측된 붓꽃의 이름 : {}'.format(iris_dataset['target_names'][prediction]))    #['setosa']


# - 하나의 입력, 특성을 가진 값이아니때문 기 에
#   아래와 같이 벡터형태로 나타내면 에러가 난다.
X_new2 = np.array([3, 4.2, 0.8, 0.4])

X_new2prediction = knn.predict(X_new2)
# ValueError: Expected 2D array, got 1D array instead:
# X_new = np.array([[3, 4.2, 0.8, 0.4]]) 이와 같은 형태의 배열이여야 한다.
# 이를 위해선 항상 데이터 형태를 확인하고 이에맞게 넣어줘야 한다.


# ### (6) 모델평가
# - 앞에서 만든 테스트 셋을 가지고
#   현재 만든 학습모델이 잘 만들어 졌는지 확인해보자

y_pred = knn.predict(X_test)
# 만들어진 학습모델은 가지고 테스트 데이터의 붓꽃품종을 예측한다.

y_pred
# 테스트 데이터의 예측 값
#array([2, 1, 0, 2, 0, 2, 0, 1, 1, 1, 2, 1, 1, 1, 1, 0, 1, 1, 0, 0, 2, 1,
#       0, 0, 2, 0, 0, 1, 1, 0, 2, 1, 0, 2, 2, 1, 0, 2])


y_pred == y_test
# 예측 품종과 실제 품종이 같으면 True
#array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
#        True,  True,  True,  True,  True,  True,  True,  True,  True,
#        True,  True,  True,  True,  True,  True,  True,  True,  True,
#        True,  True,  True,  True,  True,  True,  True,  True,  True,
#        True, False])


# 테스트 세트의 정확도
# y_pred = knn.predict(X_test)
print("테스트 세트의 정확도 : {:.4f}% ".format(np.mean(y_pred == y_test)*100))
# 97.3684% 

# knn 객체의 score 메서드 사용
print(' 테스트 세트의 정확도 : {:.4f}% '.format(knn.score(X_test,y_test)*100))
# 97.3684%

# sklearn.metrics 의 accuracy_score 사용
from sklearn import metrics

# y_pred = knn.predict(X_test)
print('테스트 세트의 정확도 : {:.4f}% '.format(metrics.accuracy_score(y_test, y_pred)*100))
# 97.3684% 


# ### (7) k값 변겅
accuracy_set = []
k_set = [1,3,5,7,9,11]

for k in k_set : 
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    accuracy_set.append(accuracy)

    
from pprint import pprint
pprint(accuracy_set)
# [0.9736842105263158,
# 0.9736842105263158,
# 0.9736842105263158,
# 0.9736842105263158,
# 0.9736842105263158,
# 0.9736842105263158]


max(accuracy_set)
# 0.9736842105263158

