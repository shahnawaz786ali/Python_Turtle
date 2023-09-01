import turtle
sa=turtle.Turtle()
sa.speed(0)
wn=turtle.Screen()
wn.bgcolor("black")
colours=['red','magenta','blue','cyan','green','yellow','white']
while True:
    for i in range(5):
        sa.color(colours[i])
        sa.pensize(3)
        sa.lt(12)
        sa.fd(200)
        sa.lt(90)
        sa.fd(200)
        sa.lt(90)
        sa.fd(200)
        sa.lt(90)
        sa.fd(200)
        sa.lt(90)
    
    