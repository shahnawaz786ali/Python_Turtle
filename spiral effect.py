from turtle import *

speed(0)
side=120
colors=["red","blue","green","cyan","black","pink"]
for i in range(200):
    width(i/200+ 1)
    color(colors[i%6])
    fd(i)
    lt(59)

        
