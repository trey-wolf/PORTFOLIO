import turtle

# DO NOT CHANGE THIS CODE BELOW
horizontal_turtle = turtle.Turtle()
vertical_turtle = turtle.Turtle()
vertical_turtle.right(90)
horizontal_turtle.penup()
vertical_turtle.penup()
# DO NOT CHANGE THIS CODE ABOVE

# --------PRACTICE--------
# Using the two turtles given to you (horizontal_turtle and vertical_turtle)
# Create a blocky letter in the middle of the screen
# You can choose whichever letter you want to do
# The only rule is you can ONLY use the two turtles given to you
# available tools forward, back, goto, penup, pendown
# WRITE YOUR CODE HERE
# Creates the letter A in blocky text
horizontal_turtle.goto(-150,200)
horizontal_turtle.pendown()
horizontal_turtle.forward(300)
vertical_turtle.goto(-150,200)
vertical_turtle.pendown()
vertical_turtle.forward(300)
horizontal_turtle.penup()
vertical_turtle.penup()
horizontal_turtle.goto(-150, 50)
horizontal_turtle.pendown()
horizontal_turtle.forward(300)
vertical_turtle.goto(150, 200)
vertical_turtle.pendown()
vertical_turtle.forward(300)
# DO NOT CHANGE THIS CODE BELOW
turtle.done()
turtle.bye()

