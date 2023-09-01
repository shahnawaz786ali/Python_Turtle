from turtle import *
import random

colormode(255)
a=random.randint(-300,300)

def square(length):
    for i in range(4):
        fd(length)
        rt(90)
        
square(100, a)