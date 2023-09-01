import turtle

sad=turtle.Turtle()
window=turtle.Screen()

sad.speed(2)
sad.pensize(3)

window.title('pattern1')
window.bgcolor('black')

list=['red','green','blue','orange','purple']

def circle():
    for i in range(10):
        sad.color(list[i%5])
        sad.circle(i*15)
 
circle()
sad.setheading(90)
circle()
sad.setheading(180)
circle()
sad.setheading(270)
circle()


    