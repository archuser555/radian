import turtle
import math

# Calculate the points in the star shape
pi = math.pi
points = [pi*2, pi/2, pi, (4*pi)/3, (5*pi)/3]
x = [math.cos(point) for point in points]  # Calculate the x coordinates
y = [math.sin(point) for point in points]  # Calculate the y coordinates

# Define the steps to draw the star shape
steps = [3, 0, 2, 4, 1, 3]
size = 100  # Size of the star

# Set up the turtle and the screen
t = turtle.Turtle()
turtle.Screen().bgcolor("red")
t.pencolor("green")
t.pensize(20)
t.up()

# Iterate through the steps and draw the star shape
for i, step in enumerate(steps):
    # Lower the pen to start drawing the star
    if i == 1:
        t.down()
    t.goto(x[step]*size, y[step]*size)  # Move the turtle to the next point

# Keep the window open until it is closed manually
turtle.mainloop()
