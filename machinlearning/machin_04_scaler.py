# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:09:00 2020

@author: USER
"""


#데이터 스케일링(Data Scaling)

#- 데이터 스케일링이랑 데이터 전처리 과정의 하나입니다.

# 데이터 스케일링을 해주는 이유는 데이터의 값이 너무 크거나 혹은 작은 경우에 
# 모델 알고리즘 학습률이 0으로 수렴하거나 무한으로 발산해버릴 수 있기 때문입니다.


# 따라서, scaling 은 데이터 전처리 과정에서 굉장히 중요한 과정이다

# 스케일링의 종류
# 1. StandardScaler
# 각 feature의 평균을 0, 분산을 1 로 변경, 모든특성들이 같은 스케일을 갖게 된다.
# 2. RubusScaler
# 모든 특성들이 같은 크기를 갖는다는 점에서 StandardScaler 와 비슷하지만
# 평균과 분산 대신 median 과 quartile 를 사용
# 3. MinMaxScaler
# 모든 feature 0과 1 사이에 위치하게 만든다.
# 데이터가 2차원 셋일 경우
# 모든 데이터는 x축의 0과 1 사이에, y축의 0과 1 사이에 위치하게 됩니다.


# Normalizer 좀 다른데 위의 셋은 통계치를 사용한다면
# 각각의 행 마다 정규화가 되는 특징
# Normalizer 는 각 각 row 마다 정규화 함.
#(유클리드 거리는 두 점 사이의 거리를 계산할 때 쓰는 방법, L2 Distance)
# 유클리드 거리가 1이 되도록 데이터를 조정.

# Normalize
# Spherical contour을 갖게 되는데, 이렇게 하면 좀 더 빠르게 학습할 수 있고 과대적합 확률을 낮출 수 있습니다.
# 스케일러는 과대적합 확률을 낮추기 위해 사용한다.
# 이 방법이 좋다 나쁘다의 개념보다 과대적합을 낮추기 위한 방법이라고 생각해 볼 수 있다.

# scikit-learn 에 있는 유방암데이터 셋으로 스케일링을 해 보자.

# scaling 작업할떄 주의할점
# scaler 내부에는 fit 과 transform 2가지가 있는데
# fit 메서드는 학습용 데이터에만 적용해야 한다
# 그 후, transform 메서드는 학습용 데이터와 테스트 데이터에 적용.



from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()

X_train, X_test, Y_train, Y_test = train_test_split(cancer.data,
                                                    cancer.target,
                                                    stratify = cancer.target,
                                                    random_state = 0)

# (1) StandardScaler
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scale = scaler.fit_transform(X_train)
# 스케일 시켜준다.
# 학습용이라 fit_transform
# 테스트용이면 그냥 transform
# 나중에 각각에 산점도 한번 찾아보라.

print('스케일 조정 전 : features MIN value : \n {}'.format(X_train.min(axis=0)))
print('스케일 조정 전 : features MAX value : \n {}'.format(X_train.max(axis=0)))
print('스케일 조정 후 : features MIN value : \n {}'.format(X_train_scale.min(axis=0)))
print('스케일 조정 후 : features MAX value : \n {}'.format(X_train_scale.max(axis=0)))


# (2) RobusScaler code
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()

X_train_scale = scaler.fit_transform(X_train)

print('스케일 조정 전 : features MIN value : \n {}'.format(X_train.min(axis=0)))
print('스케일 조정 전 : features MAX value : \n {}'.format(X_train.max(axis=0)))
print('스케일 조정 후 : features MIN value : \n {}'.format(X_train_scale.min(axis=0)))
print('스케일 조정 후 : features MAX value : \n {}'.format(X_train_scale.max(axis=0)))

# (3) MinMaxScaler code
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_train_scale = scaler.fit_transform(X_train)

print('스케일 조정 전 : features MIN value : \n {}'.format(X_train.min(axis=0)))
print('스케일 조정 전 : features MAX value : \n {}'.format(X_train.max(axis=0)))
print('스케일 조정 후 : features MIN value : \n {}'.format(X_train_scale.min(axis=0)))
print('스케일 조정 후 : features MAX value : \n {}'.format(X_train_scale.max(axis=0)))


# (4) Normalizer code
from sklearn.preprocessing import Normalizer

scaler = Normalizer()

X_train_scale = scaler.fit_transform(X_train)

print('스케일 조정 전 : features MIN value : \n {}'.format(X_train.min(axis=0)))
print('스케일 조정 전 : features MAX value : \n {}'.format(X_train.max(axis=0)))
print('스케일 조정 후 : features MIN value : \n {}'.format(X_train_scale.min(axis=0)))
print('스케일 조정 후 : features MAX value : \n {}'.format(X_train_scale.max(axis=0)))


# 머신러닝 -> 문제 답(주제)
# -> 데이터 수집 -> 데이터 스케일링 -> 최종모델 선택

# 학습시키기
# 스케일 시키기 전, 스케일 시키기 후 비교.

# SVC 로 cnacer 데이터 학습시켜보기
# 다른것들도 해볼것

from sklearn.svm import SVC
X_train, X_test, Y_train, Y_test = train_test_split(cancer.data,
                                                    cancer.target,
                                                    random_state=0)

svc = SVC()

# 스케일 하기전 데이터로 학습.
svc.fit(X_train, Y_train)

svc.score(X_test, Y_test)
#  0.9370629370629371

print('test accuracy : %.3f' % svc.score(X_test, Y_test))  # 0.937


## 스케일링 한후
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_train_scale = scaler.fit_transform(X_train)
# 학습용이라 fit_transform
X_test_scale = scaler.transform(X_test)
# test 용이라 transform

svc.fit(X_train_scale, Y_train)

print('test accuracy : %.3f' % svc.score(X_test_scale, Y_test)) # 0.972



#  KNN 으로 비교해보기
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 4)

# 스케일 하기 전 데이터로 학습.
knn.fit(X_train, Y_train)

print('test accuracy : %.3f' % knn.score(X_test, Y_test)) #0.923

#스케일 한 후
scaler = MinMaxScaler()

X_train_scale = scaler.fit_transform(X_train)
# 학습용이라 fit_transform
X_test_scale = scaler.transform(X_test)
# test 용이라 transform

knn.fit(X_train_scale,Y_train)
print('test accuracy : %.3f' % knn.score(X_test_scale, Y_test)) #0.958



### 선형 회귀로 비교해보기
from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X_train, Y_train)

print('test accuracy : %.3f' % lr.score(X_test, Y_test)) #0.729

#스케일 한 후
scaler = MinMaxScaler()

X_train_scale = scaler.fit_transform(X_train)
# 학습용이라 fit_transform
X_test_scale = scaler.transform(X_test)
# test 용이라 transform

lr.fit(X_train_scale,Y_train)
print('test accuracy : %.3f' % lr.score(X_test_scale, Y_test)) #0.729




### 의사 결정 트리 로 비교하기
from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth=3, random_state=0)

tree.fit(X_train, Y_train)

print('test accuracy : %.3f' % tree.score(X_test, Y_test)) #0.937

#스케일 한 후
scaler = MinMaxScaler()

X_train_scale = scaler.fit_transform(X_train)
# 학습용이라 fit_transform
X_test_scale = scaler.transform(X_test)
# test 용이라 transform

# 모델 세로 만들어야 한다.
tree = DecisionTreeClassifier(max_depth=3, random_state=0)

tree.fit(X_train_scale,Y_train)
print('test accuracy : %.3f' % tree.score(X_test_scale, Y_test)) #0.937



# 랜덤 포레스트
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators = 6)

forest.fit(X_train, Y_train)

print('test accuracy : %.3f' % forest.score(X_test, Y_test)) #0.937

#스케일 한 후
scaler = MinMaxScaler()

X_train_scale = scaler.fit_transform(X_train)
# 학습용이라 fit_transform
X_test_scale = scaler.transform(X_test)
# test 용이라 transform

# 모델 세로 만들어야 한다.
tree = DecisionTreeClassifier(max_depth=3, random_state=0)

tree.fit(X_train_scale,Y_train)
print('test accuracy : %.3f' % tree.score(X_test_scale, Y_test)) #0.937



#### 

# (1) StandardScaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors = 4)
knn.fit(X_train, Y_train)
print('test accuracy : %.3f' % knn.score(X_test, Y_test)) #0.923

knn.fit(X_train_scale,Y_train)
print('test accuracy : %.3f' % knn.score(X_test_scale, Y_test)) #0.958

