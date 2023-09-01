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
star.pensize(0.5)
star.hideturtle()

text=turtle.Turtle()
text.speed(6)

#text.hideturtle()
colors=['red','orange','yellow','magenta','purple','white','ivory','blue','green']

def draw_moon(pos,color):
    x,y=pos
    moon.color(color)
    moon.begin_fill()
    moon.penup()
    moon.goto(x,y)
    moon.pendown()
    moon.circle(50)
    moon.end_fill()

def draw_star(pos,color,length):
    x,y=pos
    star.color(color)
    star.penup()
    star.goto(x,y)
    star.pendown()
    star.begin_fill()
    for i in range(5):
        star.forward(length)
        star.right(144)
        star.forward(length)
    star.end_fill()

def write_text(color):
    star.color(color)
    star.penup()
    star.goto(0,0)
    star.pendown()
    style=('Stencil Std Bold',50,'normal')
    text.write('Good Night',font=style, move=True)
def random_pos():
    return(random.randint(-390,390),random.randint(-200,290))

def random_length():
    return(random.randint(5,25))

draw_moon((-300,170),'white')# call first function
draw_moon((-278,183),'black')#call the first function

while True:
    color=random.choice(colors)
    pos=random_pos()
    length=random_length()
    draw_star(pos,color,length)
    write_text(color)
turtle.done()