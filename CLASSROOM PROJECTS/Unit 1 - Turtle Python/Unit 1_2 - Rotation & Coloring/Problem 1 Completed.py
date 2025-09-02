import turtle

timmy = turtle.Turtle()
timmy.speed(5)
timmy.pensize(3)

timmy.color("blue")
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)

timmy.penup()
timmy.goto(150, 0)
timmy.pendown()

timmy.color("red")
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)

turtle.done()
turtle.bye()