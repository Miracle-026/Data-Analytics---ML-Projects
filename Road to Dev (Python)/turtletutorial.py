#!/bin/python3
"""
Turtle is a Python feature like a drawing board, which lets us command a turtle to draw all over it. We can use functions like turtle.forward(…) and turtle.right(…) which can move the turtle around.
To draw, Python turtle provides many functions and methods i.e. forward, backward, etc. Some the commonly used methods are:
	forward(x): moves the pen in the forward direction by x unit.
	backward(x): moves the pen in the backward direction by x unit.
	right(x): rotate the pen in the clockwise direction by an angle x.
	left(x): rotate the pen in the anticlockwise direction by an angle x.
	penup(): stop drawing of the turtle pen.
	pendown(): start drawing of the turtle pen.
Now to draw a circle using turtle, we will use a predefined function in “turtle”.
circle(radius): This function draws a circle of the given radius by taking the “turtle” position as the center.
"""
import turtle
#Draw a circle using Python:
t = turtle.Turtle()
r = 50
t.circle(r)
"""
Tangent Circles
A tangent is a line that touches the circumference of a circle from outside at a point, provided that any extension of the line will not cause intersection with the circle. 
Now, think about a group of circles, that have a common tangent. The group of circles, having common tangent, are known as tangent circles.
"""
#Draw tangent circles
t = turtle.Turtle()
r1 = 10
n = 10
for i in range(1, n+1, 1):
	t.circle(r1*i)