import turtle

# Create a turtle and the screen
t = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(400, 400)

# Set up the screen
screen.bgcolor("teal")
t.speed(5)
t.pensize(3)

# --- Write the birthday message ---
t.penup()
t.goto(-100, -350)
t.pendown()
t.color("purple")
t.write("Happy Birthday!", font=("Arial", 24, "bold"))

# --- Draw the filled party hat ---
# Position the turtle for the hat
t.penup()
t.goto(-300, -300)
t.pendown()

# Set hat colors
t.color("red")
t.fillcolor("orange")
t.begin_fill()

# Draw the triangle for the hat
t.forward(600)
t.left(115)
t.forward(710)
t.left(130)
t.forward(710)

t.end_fill()

# --- Draw the pom-pom on top of the hat ---
# Position the turtle for drawing the asterisk
t.penup()
t.goto(0, 343)  # Change these coordinates to draw the asterisk at a different spot
t.pendown()

# Draw the asterisk
t.color("purple")
t.right(15)
t.forward(100)
t.backward(100)
t.right(45)
t.forward(100)
t.backward(100)
t.right(45)
t.forward(100)
t.backward(100)
t.right(45)
t.forward(100)
t.backward(100)
t.right(45)
t.forward(100)
t.backward(100)
t.right(45)
t.forward(100)
t.backward(100)
t.right(45)
t.forward(100)
t.backward(100)
t.right(45)
t.forward(100)
t.backward(100)
t.right(45)

# Hide the turtle
turtle.done()
turtle.bye()
