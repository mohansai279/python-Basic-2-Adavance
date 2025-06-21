#turtle graphics using event listeners.
import turtle

# Create turtle screen and turtle object
screen = turtle.Screen()
t = turtle.Turtle()

# Define keyboard event functions
def move_forward():
    t.forward(50)

def turn_left():
    t.left(45)

def turn_right():
    t.right(45)

def clear_drawing():
    t.clear()

# Define mouse click event function
def on_click(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Set up keyboard event listeners
screen.listen()  # Start listening for key presses
screen.onkey(move_forward, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear_drawing, "c")

# Set up mouse click event listener
screen.onscreenclick(on_click)

# Keep window open
screen.mainloop()
