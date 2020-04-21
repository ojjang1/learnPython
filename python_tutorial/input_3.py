## 주로 형식이 동일한 글들에
## 데이터만 넣어서 완성본을 만들어 주는 경우.
## 매물 정보를 입력해 보자.


street = input("주소 입력 : ")
type = input("종류 입력 : ")
number_of_rooms = int(input("방 갯수 : "))
price = int(input("가격 : "))

print("####################")
print("#                  #")
print("# 부동산 매물 광고 #")
print("#                  #")
print("####################")
print("")
print(street, "에 위치한 아주 좋은 ",type, "가 매물로 나왔습니다. 이 ",type,
      "는 ", number_of_rooms, "개의 방을 가지고 있으며 가격은", price, "원 입니다")

