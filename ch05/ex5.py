# ex5.py

import turtle

sWidth, sHeight = 500, 500

turtle.title("무지개색 원 그리기")
turtle.shape("turtle")
turtle.color("white")
turtle.setup(width=sWidth + 50, height=sHeight + 50)
turtle.screensize(sWidth, sHeight)
turtle.penup()
turtle.goto(0, -sHeight / 2)  # x축 중간의 제일 아래포인트
turtle.pendown()
turtle.bgcolor("light green")
turtle.speed(10)

for radius in range(1, 250):
    if radius % 6 == 0:
        turtle.pencolor("red")
    elif radius % 5 == 0:
        turtle.pencolor("orange")
    elif radius % 4 == 0:
        turtle.pencolor("yellow")
    elif radius % 3 == 0:
        turtle.pencolor("green")
    elif radius % 2 == 0:
        turtle.pencolor("blue")
    elif radius % 1 == 0:
        turtle.pencolor("navy blue")
    else:
        turtle.pencolor("purple")

    turtle.circle(radius)

turtle.done()
