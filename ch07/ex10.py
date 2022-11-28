import turtle
import random

# 전역변수 선언
myTurtle, tx, ty, tColor, tSize, tShape = [None] * 6
# print(myTurtle) # None
shapeList = []
playerTurtle = []
sWidth, sHeight = 500, 500

# 메인 코드
if __name__ == '__main__':
  turtle.title('거북 리스트 활용')
  turtle.setup(width=sWidth + 50, height=sHeight + 50)
  turtle.screensize(sWidth, sHeight)

  shapeList = turtle.getshapes()
  # print(shapeList)
  for i in range(1, 100):
    random.shuffle(shapeList)
    myTurtle = turtle.Turtle(shapeList[0])
    # 파이썬은 화면의 정 중앙이 (0,0) 이기때문에 아래와같이 해줘야한다
    tx = random.randrange(-sWidth/2, sWidth/2)
    ty = random.randrange(-sHeight/2, sHeight/2)
    r = random.random()
    g = random.random()
    b = random.random()
    tSize = random.randrange(1, 3)
    playerTurtle.append([myTurtle, tx, ty, tSize, r, g, b]) # 100번 돌면서 100개의 리스트가 만들어짐


  # print(playerTurtle)
  for tList in playerTurtle:
    myTurtle = tList[0]
    myTurtle.color(tList[4], tList[5], tList[6])
    myTurtle.pencolor(tList[4], tList[5], tList[6])
    myTurtle.turtlesize(tList[3])
    myTurtle.goto(tList[1], tList[2])

  turtle.done()