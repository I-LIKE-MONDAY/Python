import turtle
import random

## 전역변수 선언 ##
sWidth, sHeight, pSize, exitCount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY = [0] * 7

turtle.title("거북이가 마음대로 다니기")
turtle.shape("turtle")
turtle.pensize(pSize)
turtle.setup(width=sWidth + 30, height=sHeight + 30)
turtle.screensize(sWidth, sHeight)  # 스크롤바 없어짐
turtle.color('orange')
turtle.bgcolor('lightpink')
turtle.speed(3)

while True: # 무한루프
    # 랜덤 색상
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor(r, g, b)
    x = random.randrange(1, 100)
    y = random.randrange(1, 100)

    # 랜덤 각도, 랜덤 거리
    angle = random.randrange(0, 360)
    dist = random.randrange(1, 100)
    turtle.left(angle)
    turtle.forward(dist)

    # 현재 좌표
    curX = turtle.xcor()
    curY = turtle.ycor()

    if(-sWidth / 2 <= curX <= sWidth / 2) and (-sHeight / 2 <= curY <= sHeight / 2):
        pass # 실행 안함
    else:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        exitCount += 1
        if exitCount >= 20:
            break

turtle.done()
