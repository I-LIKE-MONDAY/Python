# ex11.py

import turtle

sWidth, sHeight = 800, 450
i, k, tx, ty = [0] * 4

if __name__ == "__main__":
    turtle.title("거북이 구구단")
    turtle.shape("turtle")
    turtle.setup(width=sWidth + 50, height=sHeight + 50)
    turtle.screensize(sWidth, sHeight)
    turtle.penup()
    tx, ty = -500, 250
    turtle.goto(tx, ty)
    turtle.speed()


    for i in range(1, 10):
        for j in range(2, 10):
            turtle.goto(tx + 80 * j, ty - 40 * i)
            gugu = str(j) + "X" + str(i) + " = " + str(j * i)
            turtle.write(gugu, font=('Arial', 12, 'bold'))
turtle.done()