import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor('black')
s = turtle.Turtle()
s.speed('fastest')
s.color('white')
rotate=int(180)
def Circles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def anurag(t,size,repeat):
  for i in range (repeat):
    Circles(t,size)
    t.right(360/repeat)
anurag(s,200,10)
t1 = turtle.Turtle()
t1.speed(0)
t1.color('yellow')
rotate=int(90)
def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def anurag(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
anurag(t1,160,10)
t2= turtle.Turtle()
t2.speed(0)
t2.color('blue')
rotate=int(80)
def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def anurag(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
anurag(t2,120,10)
t3 = turtle.Turtle()
t3.speed(0)
t3.color('red')
rotate=int(90)
def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def anurag(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
anurag(t3,80,10)
t4= turtle.Turtle()
t4.speed(0)
t4.color('cyan')
rotate=int(90)
def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def anurag(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
anurag(t4,40,10)

wn.mainloop()
    
    