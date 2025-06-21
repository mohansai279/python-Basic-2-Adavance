from turtle import Turtle, Screen  # Import turtle graphics modules

# Create a screen and turtle object
s1 = Screen()
tom = Turtle()

# List of colors to use for polygons
colors = ['red', 'green', 'orange', 'yellow']

# Loop to draw polygons from 3 sides (triangle) to 8 sides (octagon)
for i in range(3, 9):
    angle = 360 / i  # Calculate internal angle for regular polygon
    tom.pencolor(colors[(i - 3) % len(colors)])  # Choose color from list cyclically

    # Draw each side of the polygon
    for _ in range(i):
        tom.forward(100)  # Move forward to draw a side
        tom.right(angle)  # Turn right to form the shape

# Exit on mouse click
s1.exitonclick()
