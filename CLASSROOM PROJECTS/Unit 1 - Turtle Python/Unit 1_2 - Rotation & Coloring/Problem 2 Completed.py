import turtle

timmy = turtle.Turtle()
timmy.speed(5)
timmy.pensize(5)

timmy.penup()
timmy.goto(0, 0)
timmy.pendown()

# North Line
timmy.color("orange")
timmy.left(90)
timmy.forward(150)

# East Line
timmy.penup()
timmy.goto(0, 0)
timmy.pendown()
timmy.color("blue")
timmy.right(90)
timmy.forward(150)

# South Line
timmy.penup()
timmy.goto(0, 0)
timmy.pendown()
timmy.color("red")
timmy.right(90)
timmy.forward(150)

# West Line
timmy.penup()
timmy.goto(0, 0)
timmy.pendown()
timmy.color("green")
timmy.left(-90)
timmy.forward(150)

# OPTIONAL EXPANSION
timmy_ext = turtle.Turtle()
timmy_ext.speed(5)
timmy_ext.pensize(3)
timmy_ext.penup()
timmy_ext.goto(0,0)
timmy_ext.pendown()

# Northeast line
timmy_ext.left(45)
timmy_ext.color("brown")
timmy_ext.forward(100)

# Southeast line
timmy_ext.penup()
timmy_ext.goto(0,0)
timmy_ext.pendown()
timmy_ext.right(90)
timmy_ext.color("purple")
timmy_ext.forward(100)

# Southwest line
timmy_ext.penup()
timmy_ext.goto(0,0)
timmy_ext.pendown()
timmy_ext.right(90)
timmy_ext.color("olive")
timmy_ext.forward(100)

# Northwest line
timmy_ext.penup()
timmy_ext.goto(0,0)
timmy_ext.pendown()
timmy_ext.right(90)
timmy_ext.color("teal")
timmy_ext.forward(100)

turtle.done()
turtle.bye()