import turtle
import math
def polygon(t, n, length):
	for i in range(n):
		t.fd(length)
		t.lt(360 / n)
def circle(radius):
	bob_circle = turtle.Turtle()
	c = 2 * math.pi * circle
	n = 50
	polygon(bob_circle, n, c / n)
	turtle.mainloop()
circle(100)

