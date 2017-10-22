import turtle
import math
def polyline(t, n, length, angle):
	for i in range(n):
		t.fd(length)
		t.lt(angle)
def arc(t, r, angle):
	arc_length = math.pi * r * angle / 180
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = angle / n
	polyline(t, n, step_length, step_angle)
def polygon(t, n, length):
	polyline(t, n, length, 360 / n)
def circle(t, r):
	arc(t, r, 360)
'''
bob = turtle.Turtle()
circle(bob, 100)
turtle.mainloop()
'''
'''
bob = turtle.Turtle()
polygon(bob, 6, 50)
turtle.mainloop()
'''

