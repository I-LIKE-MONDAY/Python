import turtle
import random

## 함수 선언 부분 ##
def screenLeftClick(x, y):
    global r, g, b  # global : 전역 변수 선언
    turtle.pencolor((r, g, b))  # penColor 에 따라 바뀜
    turtle.pendown()
    turtle.goto(x, y)

def screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)

def screenMidClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10) # 1에서 10 사이의 랜덤 값
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

pSize = 10
r, g, b = 0.0, 0.0, 0.0
turtle.title("거북이로 그림 그리기")
turtle.shape("turtle")
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()

