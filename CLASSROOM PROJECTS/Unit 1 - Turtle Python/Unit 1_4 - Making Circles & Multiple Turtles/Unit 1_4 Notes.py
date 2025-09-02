import turtle
import time

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a turtle named leo
leo = turtle.Turtle()
leo.shape("turtle")
leo.color("green")
leo.speed(1)

# --- Draw a circle ---
# The turtle will draw a complete circle with a radius of 100.
# The center of the circle will be 100 pixels to the left of the turtle's starting point.
leo.circle(100)

# Create a second turtle named don
don = turtle.Turtle()
don.shape("circle") # Give her a different shape
don.color("red")
don.pensize(5)
don.speed(1)

# --- leo's Drawing ---
leo.penup()
leo.goto(-150, 0)
leo.pendown()
leo.forward(100)
leo.right(90)
leo.forward(100)

# --- don's Drawing ---
don.penup()
don.goto(300,300)
don.pendown()
don.circle(50)

# --- Showcase of reset() ---
# Leo draws a square with a specific color and pen size
# Sets leo's speed to 1 for a slow animation
leo.speed(1)
leo.write("Leo will now draw a red square...")
time.sleep(3)
leo.undo() # Erases the previous text
leo.color("red")
leo.forward(50)
leo.left(90)
leo.forward(50)
leo.left(90)
leo.forward(50)
leo.left(90)
leo.forward(50)
leo.left(90)

leo.undo() # Erases the previous text
leo.write("Now, calling leo.reset()...")
time.sleep(3)
leo.undo() # Erases the previous text
leo.reset()  # This will clear the screen and move Leo back to the center
leo.speed(1)
time.sleep(3)
leo.write("Leo has been reset. Notice he's back at the center with default settings.")
time.sleep(3)

# --- Showcase of clear() ---
# Leo draws a simple shape
leo.undo() # Erases the previous text
leo.write("Leo will now draw a simple line...")
time.sleep(3)
leo.undo() # Erases the previous text
leo.color("blue")
leo.forward(100)
leo.right(90)
leo.forward(50)

# Clear the screen but keep Leo's position and state
leo.write("Now, calling leo.clear()...")
time.sleep(3)
leo.clear()  # This will erase the drawings but Leo stays in place
leo.write("The drawing is cleared, but Leo's position and color are unchanged.")
time.sleep(3)
leo.undo() # Erases the previous text
leo.forward(50)  # Leo will continue from his last position

# --- Showcase of undo() ---
# Leo draws a series of lines
leo.write("Leo will now draw some lines to demonstrate undo()...")
time.sleep(3)
leo.undo() # Erases the previous text
leo.penup()
leo.goto(-100, 100)
leo.pendown()
leo.color("orange")
leo.forward(50)  # Action 1
leo.right(90)
leo.forward(50)  # Action 2
leo.right(90)
leo.forward(50)  # Action 3

# Undo the last action
leo.write("Now, calling leo.undo()...")
time.sleep(3)
leo.undo() # Erases the previous text
leo.undo()  # This will erase the last line drawn
time.sleep(3)
leo.write("The last line has been undone.")
time.sleep(3)
leo.undo() # Erases the previous text

# Hide Leo once the demonstrations are complete
leo.hideturtle()
leo.write("Demonstration complete. Click the screen to exit.")

turtle.done()
turtle.bye()