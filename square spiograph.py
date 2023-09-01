import turtle
sa=turtle.Turtle()
sa.speed(0)
wn=turtle.Screen()
wn.bgcolor("black")
colours=['red','magenta','blue','cyan','green','yellow','white','red','magenta','blue','cyan','green','yellow','white','green',
         'yellow','white','red','magenta','blue','cyan','green','yellow','white','blue','cyan','green','yellow','white','red','magenta','blue','cyan','green','yellow','white','green',
         'yellow','white','red','magenta','blue','cyan','green','yellow','white']

for i in range(48):
    sa.color(colours[i])
    sa.pensize(3)
    sa.lt(8)
    sa.fd(200)
    sa.lt(90)
    sa.fd(200)
    sa.lt(90)
    sa.fd(200)
    sa.lt(90)
    sa.fd(200)
    sa.lt(90)
    sa.fd(200)
    sa.lt(90)
    sa.fd(200)
    sa.lt(90)
    sa.fd(200)
    sa.lt(90)
    sa.fd(200)
    sa.lt(90)
    