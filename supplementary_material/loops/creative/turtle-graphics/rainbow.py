import turtle  # Import the turtle graphics library

# Create turtle object
t = turtle.Turtle()  # Create a turtle object named 't'
t.speed(10)  # Set the drawing speed to a fast setting (1 slowest, 10 fastest)

# Colors and radii for the arcs
colors = ["#FF0000", "#FFA500", "#FFFF00", "#008000", "#0000FF", "#4B0082", "#EE82EE"]  # Rainbow colors
radii = [120, 130, 140, 150, 160, 170, 180]  # Radii for each arc (increasing in size)
starting_points = [10, 20, 30, 40, 50, 60, 70]  # Horizontal starting positions for each arc

# Position turtle to start drawing from the bottom, facing upward
t.left(90)  # Rotate turtle 90 degrees to face upward

# Loop through each arc to draw
for i in range(7):
  t.pen(fillcolor="black", pencolor=colors[i], pensize=10)  # Set pen color and thickness for current arc
  t.circle(radii[i], 180)  # Draw a half-circle (180 degrees) with the specified radius
  t.penup()  # Lift the pen so it doesn't draw while moving
  t.goto(starting_points[i], 0)  # Move to a new horizontal starting position at the bottom
  t.left(180)  # Flip the turtle direction to prepare for the next arc
  t.pendown()  # Lower the pen to start drawing again

# Hide turtle and keep the window open
t.hideturtle()  # Hide the turtle cursor after drawing is done
turtle.done()  # Keep the drawing window open