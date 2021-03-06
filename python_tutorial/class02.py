######## 클래스 네임스페이스####
"""
네임스페이스라는 것은
변수가 객체를 바인딩할 때
그 둘 사이의 관계를 저장하고 있는 공간을 의미.

예를 들어, 'a=2'라고 했을 때
a라는 변수는 2라는 객체가 저장된 주소를 가지고 있는데
그러한 연결 관계가 저장된 공간이 바로 네임스ㅔ이스

값을 변수에 넣을떄. 값이 있는 메모리 주소값을
변수에 넣는것이자나

파이썬의 클래스는 새로운 타입(객체)을 정의하기 위해 사용되며,
모듈과 마찬가지로 하나의 네임스페이스를 가진다.

클래스를 선언하면 클래스 에 대한 네임 스페이스가 자동으로
만들어진다.
"""

class Stock:
    market = "kospi"

print(dir())

'''
두 개의 언더바로 시작하는 것은 파이썬에서 이미 사용 중인 특별한 것들.

이를 제외하고 보면 조금 전에 정의했던 Stock 클래스의 이름이 포함된 것을
확인할 수 있다.

파이썬에서는 클래스가 정의되면 하나의 독립적인 네임스페이가 생성된다.
그리고 클래스 내의 정의된 변수나 메서드는
그 네임스페이스 안에 파이썬 딕셔너리 타입으로 저장된다.

Stock 클래스는 Stock라는 네임스페이스 안에 'market':'kospi' 라는
값을 가진 딕셔너리를 포함한다.

'''

### 파이썬 클래스 네임 스페이스
'''
Stock 클래스의 네임스페이스를 파이썬 코드로 확인하려면
클래스의 __dict__속성을 확인
'''
print('Stock__dict__ =>',Stock.__dict__)

'''
클래스가 독립적인 네임스페이스를 가지고
클래스 내의 변수나 메서드를 네임스페이스에 저장하고 있으므로
다음과 같이 클래스 내의 변수에 접근할 수 있는 것이다.
'''
print("Stock.market =>", Stock.market)

s1 = Stock()
s2 = Stock()
print("s1 = Stock() +>", id(s1))
print("s2 = Stock() +>", id(s2))
# 동일 번지값을 갖고 있는지 확인하기 위해 id() 를 이용

print(dir())

'''
s1 과 s2 인스턴스의 네임스페이스는
현재 비어 있는 것을 확인 할 수 있다.
s1,s2 는 인스턴스이고
market 는 self가 안붙어 있어 클래스 변수로 인식하므로
인스턴스로는 변수에 접근을 못한다.
'''
print("s1.__dict__ =>", s1.__dict__)
print("s2.__dict__ =>", s2.__dict__)

'''
s1 인스턴스에 market이라는 변수를 추가한 후,
다시 __dict__ 속성을 확인해 보면
'market':'kosdaq' 이라는 키 :값 쌍이 추가된 것을 볼 수 있따.
'''
s1.market = 'kosdaq'
print("s1.__dict__ =>", s1.__dict__)
print("s2.__dict__ =>", s2.__dict__)


'''
만약 s1.market, s2.market 과 같이
인스턴스를 통해 market이라는 값에 접근하면?
'''
print("s1.market=>",s1.market)
print("s2.market=>",s2.market)

'''
s2 인스턴스를 통해 변수에 접근하면
파이썬은 먼저
s2인스턴스의 네임스페이스에서 해당 변수가 존재하는지 찾는다.

만약 s2의 네임스페이스에 해당 변수가 존재하지 않으면
s2 인스턴스의 클래스 네임스페이스로 가서 다시 변수를 찾게 된다.

즉,
s2.market이라는 문장이 실행되면
Stock 클래스의 네임스페이스에 있는
'market':'kospi'
키:값 쌍에서 'kospi' 라는 문자열을 출력하게 된다.
'''



