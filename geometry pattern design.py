import turtle

turtle.shape("turtle")

turtle.colormode(255)
turtle.color(120,50,100)

turtle.speed(0)

def hexagon(length,sides):
    for i in range(sides):
        turtle.fd(length)
        turtle.rt(360/sides)
        
def pattern(length,sides):
    for i in range(sides):
        hexagon(length,sides)
        turtle.fd(length)
        turtle.lt(360/sides)
        
pattern(50,10)

turtle.hideturtle()