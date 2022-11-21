import turtle

myT = None

myT = turtle.Turtle()
myT.shape("classic")

for i in range(0, 100): # 선언부
    myT.forward(200) # Body
    myT.right(90)

turtle.done