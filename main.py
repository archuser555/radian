# Just draw a star with math and python LOL
import turtle
import math

pi = math.pi
points = [pi*2, pi/2, pi, (4*pi)/3, (5*pi)/3] # points...
steps = [3, 0, 2, 4, 1, 3] # Here is the cordinates from x & y that will form the star shape
x = []
y = []
i = 0

while True:
    if(i > len(points)-1):
        break
    x.append(math.cos(points[i]))
    y.append(math.sin(points[i]))
    i += 1

t = turtle.Turtle()
t.down()
i = 0
#Doing Moves...
while i < len(steps):
    t.goto(x[steps[i]]*50, y[steps[i]]*50)
    i += 1
    print(i)

turtle.mainloop()