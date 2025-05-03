import turtle

# Set up the screen (optional)
screen = turtle.Screen()
screen.bgcolor("white")

# Initialize the turtle
franklin = turtle.Turtle()

# Set the speed to maximum (optional)
franklin.speed(10)

# Draw a square using a loop
for _ in range(4):
    franklin.forward(100)
    franklin.right(90)

# Finish the drawing
turtle.done()