import turtle
import time

love = 'Hanpier bro'
def rotate():
    turtle.speed(0)  
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)

turtle.setup(width = 800,height = 500)
turtle.color('yellow','pink')
turtle.pensize(3)
turtle.speed(2)

turtle.hideturtle()
turtle.up()
turtle.goto(0,-180)
turtle.down()
turtle.left(140)
turtle.showturtle()
turtle.begin_fill()

turtle.forward(224)
rotate()
turtle.left(120)
rotate()
turtle.forward(224)

time.sleep(0.8)
turtle.end_fill()

turtle.hideturtle()
turtle.up()
turtle.goto(0,0)
turtle.down()
turtle.hideturtle()
turtle.color('#CD5C5C', 'pink')

time.sleep(0.5)
turtle.write(love, font=('times new roman', 30, 'bold'), align="center")

turtle.done()
