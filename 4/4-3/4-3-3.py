def polygon(t, length, n):
	for i in range(n):
		t.fd(length)
		t.lt(360 / n)
import turtle
bob = turtle.Turtle()
polygon(bob, 50, 12)
turtle.mainloop()
