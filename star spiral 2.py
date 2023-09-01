from turtle import *
import random
speed(0)

def a(n):
    for x in range(n):
        colormode(255)
        a=random.randint(1,255)
        b=random.randint(1,255)
        c=random.randint(1,255)
        pencolor(a,b,c)
        begin_fill()
        fillcolor(a,b,c)
        for i in range(5):
            fd(5*n-5*x)
            rt(144)
            fd(5*n-5*x)
            lt(72)
        end_fill()
        rt(10)
        
a(36)
