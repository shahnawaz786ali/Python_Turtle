#draw a shape and fill the colour
import turtle
sa=turtle.Turtle()
for i in range(2):
    sa.begin_fill()
    sa.fillcolor('Red')
    sa.fd(200)
    sa.lt(90)
    sa.fd(100)
    sa.lt(90)
    sa.end_fill()