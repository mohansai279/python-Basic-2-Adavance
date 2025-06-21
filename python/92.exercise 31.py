#we will design a painting of random dots on canvas using turtle graphics. Search "Hirst dot painting" for reference.
from turtle import Turtle, Screen
import random

# Setup
s1 = Screen()
s1.colormode(255)  # Use RGB colors
s1.bgcolor("white")
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

# Define color palette (you can customize this!)
color_palette = [
    (239, 71, 111),  # pink/red
    (255, 209, 102),  # yellow
    (6, 214, 160),    # mint green
    (17, 138, 178),   # teal
    (7, 59, 76),      # dark blue
    (255, 127, 80),   # coral
    (142, 68, 173),   # purple
    (26, 188, 156),   # turquoise
]

# Starting position
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# Dot painting layout
dots_per_row = 10
total_rows = 10
dot_size = 20
spacing = 50

for row in range(total_rows):
    for dot in range(dots_per_row):
        tim.dot(dot_size, random.choice(color_palette))
        tim.forward(spacing)
    tim.setheading(90)
    tim.forward(spacing)
    tim.setheading(180)
    tim.forward(spacing * dots_per_row)
    tim.setheading(0)

s1.exitonclick()
