import turtle  # Import the turtle graphics module

bob = turtle.Turtle()  # Create a new turtle object named 'bob'
bob.speed(20)  # Set the turtle's drawing speed (1 is slow, 10 is fast, 20 is very fast)

bob.color("red", "yellow")  # Set the turtle's pen color to red and fill color to yellow

bob.begin_fill()  # Begin filling the shape with the yellow color
for _ in range(250):  # Loop 250 times to draw the pattern
  bob.forward(150)  # Move the turtle forward by 150 units
  bob.left(175)  # Turn the turtle left by 175 degrees

bob.end_fill()  # End the filling of the shape

turtle.done()  # Finish the turtle graphics and display the result