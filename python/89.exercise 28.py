#we will draw a dashed line using turtle graphics in python.
from turtle import Turtle, Screen

s1 = Screen()
tom = Turtle()

# Draw dashed line
for _ in range(10):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()
    tom.pencolor("green,red")
s1.exitonclick()

# tom.penup()
# tom.forward(10)
# tom.pendown()
# tom.forward(10)
# tom.penup()
# tom.forward(10)
# tom.pendown()
# tom.forward(10)
# tom.penup()
# tom.forward(10)
# tom.pendown()
# tom.forward(10)
# tom.penup()
# tom.forward(10)
# tom.pendown()
# tom.forward(10)
# tom.penup()
# tom.forward(10)
# tom.pendown()


