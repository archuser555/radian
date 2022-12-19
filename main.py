# Just draw a star with math and python LOL
import turtle
import math

pi = math.pi
points = [pi*2, pi/2, pi, (4*pi)/3, (5*pi)/3] # points...
steps = [3, 0, 2, 4, 1, 3] # Here is the cordinates from x & y that will form the star shape
size = 100 #size of star
x = []
y = []
i = 0

while True:
    if(i > len(points)-1):
        break
    x.append(math.cos(points[i]))
    y.append(math.sin(points[i]))
    i += 1

#setup something's
t = turtle.Turtle()
turtle.Screen().bgcolor("red")
t.pencolor("green")
t.pensize(20)
t.up()
i = 0
#Doing Moves...
while i < len(steps):
    if(i == 1):
    	t.down() #this fix a small issue while drawing the start
    t.goto(x[steps[i]]*size, y[steps[i]]*size)
    i += 1
    print(i)

turtle.mainloop()
