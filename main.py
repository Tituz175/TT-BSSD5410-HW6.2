import turtle


def koch(t, order, size):
    """
    Make turtle t draw a KocH fractal of 'order' and 'size'.
    Leave the turtle facing the same direction.
    :param t:
    :param order:
    :param size:
    :return:
    """

    if order == 0:
        t.forward(size)
    else:
        koch(t, order - 1, size / 3)
        t.left(60)
        koch(t, order - 1, size / 3)
        t.right(180)


def main():
    size = 1000
    screen = turtle.Screen()
    screen.setup(size + 20, size + 20)
    screen.screensize(size, size)
    screen.bgcolor("#94e396")
    screen.title("Koch Snowflake")
    turtle.penup()
    turtle.goto(-size / 8, size / 12)
    turtle.pendown()
    turtle.color("#4776c7")
    turtle.pensize(2)
    turtle.shape(None)
    for i in range(3):
        koch(turtle, 4, 2000)
        turtle.right(120)
    turtle.done()


if __name__ == "__main__":
    main()
