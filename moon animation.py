#draw good night annimation
import turtle
import random
wn=turtle.Screen()
wn.setup(width=800,height=600)
wn.bgcolor('black')
wn.title('good night annimation')
moon=turtle.Turtle()
moon.hideturtle()
star=turtle.Turtle()
star.speed(0)
star.hideturtle()
text=turtle.Turtle()
text.speed(6)
text.hideturtle()
def draw_moon(pos,color):
    x,y=pos
    moon.color(color)
    moon.begin_fill()
    moon.penup()
    moon.goto(x,y)
    moon.pendown()
    moon.circle(50)
    moon.end_fill()
draw_moon((-300,170),'white')
draw_moon((-278,183),'black')
    



