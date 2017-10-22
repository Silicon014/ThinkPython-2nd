def circle(t, r, arc):
	n = 36
	for i in range(n * arc / 360):
		t.fd(2 * math.pi * r / n)
		t.lt(360 / n)
import math
import turtle
bob = turtle.Turtle()
circle(bob, 100, 240)
turtle.mainloop()
