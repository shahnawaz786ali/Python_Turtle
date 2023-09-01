#draw a shape and increse speed of pen and pensize 
import turtle
sa=turtle.Turtle()

sa.pensize(3)# pensize
sa.speed(0)#penspeed
colour=['blue','black','red','purple','pink','orange','brown']
radius=[50,45,40,35,55,60,65]
def circle():
    for i in range(7):
        sa.circle(radius[i])
        sa.pencolor(colour[i])
circle()
radius=[-50,-45,-40,-35,-55,-60,-65]
def circle1():
    for i in range(7):
        sa.circle(radius[i])
        sa.pencolor(colour[i])
sa.lt(90)
circle1()
sa.lt(180)
circle()
sa.lt(90)
circle1()
