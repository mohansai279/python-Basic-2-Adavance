#(Turtle Star and Spirograph) using different colors using turtle graphics in python.
from turtle import Turtle, Screen

# Set up the screen and turtle
s1 = Screen()
tom = Turtle()

# Set the pen color (one color)
tom.color("red")

# Draw the star pattern
for _ in range(50):
    tom.forward(200)
    tom.left(170)

# Keep the window open until a click
s1.exitonclick()

