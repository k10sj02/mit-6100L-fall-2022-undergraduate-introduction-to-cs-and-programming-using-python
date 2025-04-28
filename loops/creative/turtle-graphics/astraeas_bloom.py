import turtle  # Import the turtle graphics module

yoshi = turtle.Turtle()  # Create a new turtle object named 'yoshi'
yoshi.speed(20)  # Set the turtle's drawing speed (1 is slow, 10 is fast, 20 is very fast)

def star(yoshi, size):  # Define a function to draw a star with recursion
  if size <= 10:  # Base case: if the size is too small, stop drawing
    return
  else:
    for _ in range(5):  # Loop 5 times to draw the 5 points of the star
      yoshi.forward(size)  # Move the turtle forward by 'size' units
      star(yoshi, size/2)  # Recursively call the star function with half the size
      yoshi.left(216)  # Turn the turtle left by 216 degrees to form the star shape

star(yoshi, 365)  # Call the star function with the initial size of 365

turtle.done()  # Finish the turtle graphics and display the result