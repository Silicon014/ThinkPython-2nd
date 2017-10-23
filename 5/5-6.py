import turtle


def koch(t, x):
    if x < 3:
        t.fd(x)
        return
    koch(t, x / 3)
    t.lt(60)
    koch(t, x / 3)
    t.rt(120)
    koch(t, x / 3)
    t.lt(60)
    koch(t, x / 3)


def snowflake(t, length):
    for i in range(3):
        koch(t, length)
        t.rt(120)


def main():
    n = int(input("enter the length of an edge of the snowflake: "))
    t = turtle.Turtle()
    snowflake(t, n)
    turtle.mainloop()


main()
