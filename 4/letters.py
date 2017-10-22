import turtle
import math
def polyline(t, n, l, a):
	for i in range(n):
		t.fd(l)
		t.lt(a)
def arc(t, r, a):
	l = a / 180 * math.pi * r
	n = int(l / 3) + 1
	step_l = l / n
	step_a = a / n
	polyline(t, n, step_l, step_a)
def draw_a(t):
	l = 50
	t.lt(90)
	t.fd(50)
	t.lt(90)
	arc(t, l / 2, 150)
	t.lt(60)
	t.fd(l / 2 / math.sqrt(3))
	t.rt(120)
	t.fd(l / 2 / math.sqrt(3))
	t.lt(90)

bob = turtle.Turtle()
draw_a(bob)
turtle.mainloop()

