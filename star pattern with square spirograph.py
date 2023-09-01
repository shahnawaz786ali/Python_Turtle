import turtle

sa = turtle.Turtle()
sa.speed(0)
side = 200
for i in range(100):
   sa.forward(side)
   sa.right(144) #Exterior angle of a star is 144 degree
   side = side - 2
sa.penup()
sa.goto(-130,100)
sa.pendown()
sa.pencolor('magenta')
for i in range(100):
   sa.forward(side)
   sa.right(90) #Exterior angle of a square is 90 degree
   side = side - 2
sa.penup()
sa.goto(-350,-160)
sa.pendown()
sa.pencolor('red')
# side1=100
for i in range(70):
   sa.forward(side)
   sa.right(120) #Exterior angle of a triangle is 120 degree
   side = side- 2