import turtle
import math
def triangle(t, r, l, a):
	t.fd(r)
	t.lt(90 + a / 2)
	t.fd(l)
	t.lt(90 + a / 2)
	t.fd(r)
	t.lt(180)
def polygon(t, r, n):
	l = math.pi * 2 * r / n
	a = 360 / n
	for i in range(n):
		triangle(t, r, l, a)
#start:
bob = turtle.Turtle()
#polygon(bob, 100, 6)
#polygon(bob, 100, 12)
polygon(bob, 200, 72)
turtle.mainloop()
