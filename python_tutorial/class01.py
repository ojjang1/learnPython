#클래스 내부에 정의된 함수인 메서드의 첫 번쨰 인자는 반드시 self 여야 한다.

class BusinessCard:

    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print("-----------------")
        print("Name : ", self.name)
        print("email : ", self.email)
        print("Address : ",self.addr)
        print("-----------------")

    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

## self 이해하기
class Foo:
    def func1():
        print("function1")

    def func2(self):
        print(id(self))
        print("function2")
## 함수에 오류가 있어도 클래스 생성, 실행이나, 클래스 호출때는 문제가 생기지 않는다.
'''
Foo 클래스의 func2 메서드는
메서드의 인자가 self뿐이므로
실제 메서드를 호출할 때는 인자를 전달할 필요가 없다.

func2 메서드의 첫 번쨰 인자는 self지만
호출할 떄는 아무것도 전달하지 않는 이유는
첫 번쨰 인자만 self에 대한 값은
파이썬이 자동으로 넘겨주기 때문.

func1 메서드 처럼
메서드를 정의할 때부터 아무 인자도 없는 경우에는
인스턴스를 통해 func1()을 호출해보면 오류가 발생

오류 메시지:
func() dakes() positional arguments but 1 was given

오류 메시지를 살펴보면
"func() 은 인자가 없지만 하나를 받았따."
라고 알 수 있다.

self 의 정체를 좀 더 확실히 밝혀보기 위해
Foo 클래스를 수정하여 파이썬 내장 함수인 id()를 이용해
인스턴스가 메모리에 할당된 주소값을 확인.

>>> f = Foo()
>>> f.func2()
57066616
function2
>>> id(f)
57066616

실행 결과를 살펴보면 객체의 값과
함수 안에 self 의 아이디 값이 같은것을 볼 수 있다.
객체생성 할떄 self 변수로 값이 넘어 간것.

>>> f2 = Foo()
>>> id(f2)
57066544
>>> f2.func2()
57066544
function2

f2를 통해 func2 메서드를 호출해보면 새로운 객체 값으로
만든것을 알 수 있따.
'''

'''
파이썬의 클래스는 그 자체가 하나의 네임스페이스 이기 떄문에
인스턴스 생성과 상관없이
클래스 내의 메서들를 직접 호출 할 수 있다.
Java의 static 과 같은 느낌

Foo.func1()
이건 오류 발생이 안난다.
클래스 자체로 접근 한거라 self 인자가 필요없기 때문
Foo.func2() 로 호출하면 오류 발생.
self 위치에 인자를 전달하지 않고 메서드를 호출하면 오류가 발생

즉 클래스 명 자체로 함수 호출할떄는
매개변수에 self 가 필요없고

객체를 호출해서 함수를 사용하려할때는
함수 안에 self를 꼭 넣어 주어야 한다.

'''


'''
f3 = Foo()

Foo.func2(f3)
f3.func2()

func2 메서드는 인자를 하나 필요로 하며, 해당 인자는 인스턴스여야 한다.

현재 f3은 새로 생성한 인스턴스를 바인딩하고 있으므로
func2 메서드의 인자로 f3을 전달해주면 된다... 

'''
