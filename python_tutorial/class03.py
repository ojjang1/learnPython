### 클래스 변수와 인스턴스 변수
'''
은행 계좌를 클래스로 표현

Account 클래스
생성저(__init__):클래스의 인스턴스가 생성될 때 자동으로 호출되는 함수
소멸자(__del__): 클래스의 인스턴스가 소멸될 떄 자동으로 호출되는 함수
'''

class Account:
    num_accounts = 0
    def __init__(self,name):
        self.name = name
        Account.num_accounts +=1

    def __del__(self):
        Account.num_accounts -= 1

## num_accounts 는 클래스 변수 라서 클래스명. 으로 접근
## name 는 앞에 self. 가 붙어있으므로 반드시 객체명 으로 접근

'''
num_accounts와 self.name이라는 두 종류의 변수가 존재.

num_accounts와 같이 클래스 내부에 선언된 변수를 클래스 변수.
self.name과 같이 self가 붙어 있는 변수를 인스턴스 변수.

여러 인스턴스간에 서로 귱유해야 하는 값은 클래스 변수를 통해 바인딩
'''
kim = Account("kim")
lee = Account("lee")

# 소유자 정보는 인스턴스 변수인 name 이 바인딩

print("kim.name =>",kim.name)
print("lee.name =>",lee.name)

'''
먼저 인스턴스의 네임스페이스에서
num_accounts 를 찾았지만 해당 이름이 없어서

클래스의 네임스페이스로 이동한 후,
다시 해당 이름을 찾았고
그 값이 변환된 것
'''
print("kim.nemaccousts =>",kim.num_accounts)
print("lee.nemaccousts =>",lee.num_accounts)
