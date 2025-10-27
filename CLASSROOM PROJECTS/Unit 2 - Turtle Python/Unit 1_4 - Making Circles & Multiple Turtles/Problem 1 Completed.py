import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("gray")
turtle.colormode(255)

# Create the turtle
t = turtle.Turtle()
t.pensize(3)
t.speed(5)
t.hideturtle()

# --- Draw the traffic light box ---
t.penup()
t.goto(60, -60)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.right(-90)
t.forward(250)
t.right(-90)
t.forward(120)
t.right(-90)
t.forward(250)
t.right(-90)
t.forward(120)
t.end_fill()

# --- Draw the red light ---
t.penup()
t.goto(0, 100)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(35)
t.end_fill()

# --- Draw the yellow light ---
t.penup()
t.goto(0, 30)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(35)
t.end_fill()

# --- Draw the green light ---
t.penup()
t.goto(0, -40)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.circle(35)
t.end_fill()

# --- Write the text for the lights ---
t.penup()
t.goto(-20, 115)
t.pendown()
t.color("white")
t.write("STOP", font=("Arial", 14, "bold"))

t.penup()
t.goto(-20, 45)
t.pendown()
t.write("SLOW", font=("Arial", 14, "bold"))

t.penup()
t.goto(-20, -25)
t.pendown()
t.write("GO", font=("Arial", 14, "bold"))

# OPTIONAL EXTENSION
# 1. Green arrow for dedicated turn to left
# 2. Instead of just drawing the traffic light, animate it over time
#    Have it start with a green arrow / green solid circle for 10 seconds
#    then go to yellow for 5 seconds
#    Then red for 15 seconds

# Keep the window open
turtle.done()