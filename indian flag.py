import turtle
x = turtle.Turtle()
x.goto(0,-300)
x.goto(0,300)

def rect(color):
    x.begin_fill()
    x.fillcolor(color)
    for i in range(2):
        x.fd(250)
        x.rt(90)
        x.fd(50)
        x.rt(90)
    x.end_fill()

rect("orange")
x.up()
x.goto(0,250)
x.down()
rect("white")
x.fd(125)
x.circle(-25)
x.rt(90)
x.fd(25)
x.lt(90)
for i in range(24):
    x.fd(25)
    x.bk(25)
    x.lt(15)
x.up()
x.goto(0,200)
x.down()
rect("green")
x.hideturtle()