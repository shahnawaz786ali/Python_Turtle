import turtle
sa=turtle.Turtle()
sa.begin_fill()
sa.fillcolor('purple')
for i in range(4):
    sa.fd(200)
    sa.lt(90)
sa.end_fill()
sa.rt(60)
sa.begin_fill()
sa.fillcolor('red')
def equilateral():
    for i in range(2):
        sa.fd(200)
        sa.rt(-120)
equilateral()
sa.end_fill()
colour=['magenta','red','black']
for i in range(3):
    sa.begin_fill()
    sa.fillcolor(colour[i])
    sa.rt(150)
    equilateral()
    sa.end_fill()
    
