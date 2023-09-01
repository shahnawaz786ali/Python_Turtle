import turtle

def petal(t, r, angle):
    """Use the Turtle (t) to draw a petal using two arcs
    with the radius (r) and angle.
    """
    for i in range(2):
        t.circle(r,angle)
        t.left(180-angle)

def flower(t, n, r, angle):
    """Use the Turtle (t) to draw a flower with (n) petals,
    each with the radius (r) and angle.
    """
    for i in range(n):
        petal(t, r, angle)
        t.left(360.0/n)

def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Pen()

# draw a sequence of three flowers, as shown in the book.
# I've added color and fill

#remember to speed up your turtle
bob.speed(0)

bob.color("red")
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

bob.color("green")
move(bob, 100)
flower(bob, 10, 40.0, 80.0)

bob.color("blue")
move(bob, 100)
flower(bob, 20, 140.0, 20.0)

# now draw them filled
bob.pu()
bob.goto(0,150)
bob.color("red")
bob.fill(1)
move(bob, -100)
flower(bob, 7, 60.0, 60.0)
bob.fill(0)

bob.color("green")
bob.fill(1)
move(bob, 100)
flower(bob, 10, 40.0, 80.0)
bob.fill(0)

bob.color("blue")
bob.fill(1)
move(bob, 100)
flower(bob, 20, 140.0, 20.0)
bob.fill(0)

# you could also draw them outlined
bob.pu()
bob.goto(0,300)
move(bob, -100)
bob.color("yellow")
bob.fill(1)
move(bob, 100)
flower(bob, 10, 40.0, 80.0)
bob.fill(0)
bob.color("black")
bob.width(1)
flower(bob, 10, 40.0, 80.0)

turtle.exitonclick()