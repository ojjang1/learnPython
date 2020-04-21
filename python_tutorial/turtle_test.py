import turtle
colors=["red","purple","blue","green","yellow","orange"]
t=turtle.Turtle()
# turtle 모듈 안에 Turtle() 라는 생성자를 호출
# 그걸 t라는 변수에 대임
# 이 객체를 통해 안에 함수를 사용한다.
# bgcolor 은 해당 객체 안이 아니라 모듈 안에 정의도이었으므로
# 모듈 자체로 접근한다.
# speed, width 는 객체 내 함수라서 접근

turtle.bgcolor("black")
t.speed(0)
t.width(3)
length = 10

while length < 500:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length +=5

# pencolor 은 위에서 선언한 색 중에서
# 6으로 나눴으니까 0,1,2,3,4,5 중에서 나오겠지
# 
