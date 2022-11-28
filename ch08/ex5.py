"""
  title : 거북 글자 쓰기
  filename : ex4.py
  author : Gwak
  date : 22.11.28
"""

# 거북 글자 쓰기
import math
import turtle
import random
from tkinter.simpledialog import *

# 전역변수 선언
inStr = ''
sWidth, sHeight = 500, 500
tx, ty, tSize = [0] * 3

turtle.title('나선 모양의 거북 글자 쓰기')
turtle.shape('turtle')
turtle.setup(width=sWidth + 50, height=sHeight + 50)
turtle.screensize(sWidth, sHeight)
turtle.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열 입력')

dist = 200
angle = 0
value = int(360 * 4 / len(inStr))
for ch in inStr:
  rad = 3.141592 * angle / 180
  tX = dist * math.cos(rad)
  tY = dist * math.sin(rad)
  dist -= 200 / len(inStr)
  angle += value

  r = random.random()
  g = random.random()
  b = random.random()

  turtle.goto(tX, tY)
  turtle.pencolor((r, g, b))
  turtle.write(ch, font=('맑은고딕', 20, 'bold'))

turtle.done()