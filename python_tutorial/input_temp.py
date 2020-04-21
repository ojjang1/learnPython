## 화씨 온도를 섭씨 온도로 변환하기
print("화씨온도를 섭씨온도로 변환합니다")
ftemp = int(input("화씨온도: "))
ctemp = (ftemp-32.0)*5.0/9.0
print("섭씨온도 :", ctemp)


# 섭씨온도를 화씨 온도로 변환하기
print("")
print("섭씨온도를 화씨온도로 변환합니다.")
ctemp = int(input("섭씨 온도: "))
ftemp = ctemp*9/5+32
print("화씨온도 : ", ftemp)
