# Import the turtle graphics library
import turtle

# Create a turtle object and a screen object
t = turtle.Turtle()
s = turtle.Screen()

# Set the background color of the window to black
s.bgcolor("black")

# Set the width of the turtle's pen
t.width(2)

# Set the speed of the turtle (higher means faster)
t.speed(15)

# Define a tuple of three colors to cycle through
col = ("white", "pink", "cyan")

# Draw 300 lines in a pattern
for i in range(300):
    # Set the pen color by cycling through the color list
    t.pencolor(col[i % 3])
    # Move the turtle forward; distance increases each time
    t.forward(i * 4)
    # Turn the turtle right by 121 degrees
    t.right(121)

turtle.done()