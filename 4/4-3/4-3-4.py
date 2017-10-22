def circle(t, r):
	n = 36
	for i in range(n):
		t.fd(2 * math.pi * r / n)
		t.lt(360 / n)
import math
import turtle
bob = turtle.Turtle()
circle(bob, 100)
turtle.mainloop()
