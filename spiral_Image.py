import turtle


def draw_spiral():
    """Draws a spiral using turtle graphics."""
    # Initialize variables that will control the spiral's shape and growth
    distance = 0
    angle = 0

    turtle.bgcolor("black")
    turtle.speed(0)  # Fastest speed
    turtle.pencolor("green")

    turtle.penup()
    turtle.goto(0, 200)
    turtle.pendown()

    while True:
        turtle.forward(distance)
        turtle.right(angle)
        distance += 3
        angle += 1

        # Change color and check for exit condition
        if angle == 100:
            turtle.pencolor("red")

        if angle == 200:
            break

    turtle.exitonclick()


if __name__ == "__main__":
    draw_spiral()
