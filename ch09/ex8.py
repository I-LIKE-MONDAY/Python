from myTurtle import *
import turtle

# 전역변수 선언
inStr = ''
sWidth, sHeight = 300, 300
tx, ty, tAngle, txtSize = [0] * 4

turtle.title('거북 글자 쓰기(모듈 버전)')
turtle.shape('turtle')
turtle.setup(width=sWidth + 50, height=sHeight + 50)
turtle.screensize(sWidth, sHeight)
turtle.penup()
turtle.speed(5)

inStr = getString()

for ch in inStr:
  tx, ty, tAngle, txtSize = getXYAS(sWidth, sHeight)
  r, g, b = getRGB()

  turtle.goto(tx, ty)
  turtle.left(tAngle)
  turtle.pencolor((r, g, b))
  turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))

