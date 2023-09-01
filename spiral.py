import turtle

window=turtle.Screen()
window.colormode(255)
window.bgcolor(100,50,250)

window.title("spiral")

turtle.speed(0)

def draw_spiral(radius):
    '''original_xcor = turtle.xcor()
    original_ycor = turtle.ycor()'''
    speed = 1
    while True:
        turtle.forward(speed)
        turtle.left(10)
        speed += 0.1
       # if turtle.distance(original_xcor,original_ycor)>radius:
           # break
        
        
draw_spiral(100)