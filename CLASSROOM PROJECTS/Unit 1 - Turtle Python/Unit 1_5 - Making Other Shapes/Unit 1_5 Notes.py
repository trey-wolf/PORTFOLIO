import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightgrey")
screen.title("Raphael's Polygon and Arc Showcase")

# Create the turtle
raphael = turtle.Turtle()
raphael.shape("turtle")
raphael.pensize(3)
raphael.speed(3)
raphael.hideturtle()

# --- Draw a Triangle (3 sides) ---
raphael.penup()
raphael.goto(-250, 0)
raphael.pendown()
raphael.color("red")
raphael.showturtle()
raphael.circle(50, extent=360, steps=3)
raphael.hideturtle()

# --- Draw a Square (4 sides) ---
raphael.penup()
raphael.goto(-100, 0)
raphael.pendown()
raphael.color("blue")
raphael.showturtle()
raphael.circle(50, extent=360, steps=4)
raphael.hideturtle()

# --- Draw a Hexagon (6 sides) ---
raphael.penup()
raphael.goto(50, 0)
raphael.pendown()
raphael.color("green")
raphael.showturtle()
raphael.circle(50, extent=360, steps=6)
raphael.hideturtle()

# --- Draw a Semicircle (180 degrees) ---
raphael.penup()
raphael.goto(150, 0)
raphael.pendown()
raphael.begin_fill()
raphael.color("purple")
raphael.showturtle()
raphael.circle(100, extent=180)
raphael.end_fill()
raphael.hideturtle()

# --- Draw a Quarter Circle (90 degrees) ---
raphael.penup()
raphael.goto(250, 0)
raphael.pendown()
raphael.begin_fill()
raphael.color("orange")
raphael.showturtle()
raphael.circle(100, extent=90)
raphael.end_fill()
raphael.hideturtle()

# Keep the window open
turtle.done()
turtle.bye()