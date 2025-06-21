import turtle as t
import random
import time

screen = t.Screen()
screen.bgcolor("lightgreen")
screen.title("Turtle Race 🐢🏁")

# Create 2 turtles with different shapes and colors
t1 = t.Turtle()
t1.shape("turtle")
t1.color("red")
t1.penup()
t1.goto(-200, 100)  # Start position
t1.pendown()

t2 = t.Turtle()
t2.shape("turtle")
t2.color("blue")
t2.penup()
t2.goto(-200, -100)  # Start position
t2.pendown()

# Draw finish line
line = t.Turtle()
line.hideturtle()
line.penup()
line.goto(200, 150)
line.right(90)
line.pendown()
line.forward(300)

# Start the race
print("Race starting...")
time.sleep(1)

for i in range(50):
    t1.forward(random.randint(1, 10))
    t2.forward(random.randint(1, 10))
    time.sleep(0.05)

# Announce winner
if t1.xcor() > t2.xcor():
    print("Red turtle wins! 🏆")
elif t2.xcor() > t1.xcor():
    print("Blue turtle wins! 🏆")
else:
    print("It's a tie!")

t.exitonclick()
