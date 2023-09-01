import turtle
import random

turtle.bgcolor("green")
turtle.title("Turtle Race game")

t1=turtle.Turtle()
t1.up()
t1.goto(-300,40)
t1.color("red")
t1.shape("turtle")

t2=turtle.Turtle()
t2.up()
t2.goto(-300,-40)
t2.color("magenta")
t2.shape("turtle")

turtle.up()
turtle.goto(-280, 60)
turtle.down()

turtle.begin_fill()
turtle.fillcolor("black")
for i in range(2):
    turtle.fd(600)
    turtle.rt(90)
    turtle.fd(120)
    turtle.rt(90)
    
turtle.end_fill()

while True:
    
    t1.fd(random.randint(1,10))
    t2.fd(random.randint(1,10))
    
    if t1.pos() > (300, 40):
        t1.write("Turtle1 is winner",align="right", font=("normal", 20, "bold"))
        break
    if t2.pos() > (300,-40):
        t2.write("Turtle2 is winner", align="right",font=("normal", 20, "bold"))
        break
    