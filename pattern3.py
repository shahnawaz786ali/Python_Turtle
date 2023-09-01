import turtle

sad=turtle.Turtle()
window=turtle.Screen()

sad.speed(2)
sad.pensize(3)

window.title('pattern1')
window.bgcolor('black')

sad.color('red')


def circle():
    for i in range(10,5,-1):
        sad.circle(i*10)

circle()
sad.setheading(70)
circle()
sad.setheading(140)
circle()
sad.setheading(210)
circle()
sad.setheading(280)
circle()
