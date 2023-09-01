import turtle
 
# function to draw
# colored star
def colored_star():
     
    # object color
    turtle.color("red")
     
    # object width
    turtle.width(4)
     
    # color to fill
    turtle.fillcolor("yellow")
    turtle.begin_fill()
     
    # form star
    for side in range(5):
        turtle.forward(120)
        turtle.right(120)
        turtle.forward(120)
        turtle.right(72 - 120)
         
    # fill color
    turtle.end_fill()
 
# Driver code
colored_star()