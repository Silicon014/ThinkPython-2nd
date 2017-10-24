import turtle


def draw(t, n, l):
    '''
    用来画一个边长为l的正n边形
    '''
    for i in range(n):
        t.lt(360 / n)
        t.fd(l)


a = turtle.Turtle()
draw(a, 12, 50)
turtle.mainloop()
