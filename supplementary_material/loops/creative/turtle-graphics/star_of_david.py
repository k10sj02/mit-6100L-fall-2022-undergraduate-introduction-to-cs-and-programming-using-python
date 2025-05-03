import turtle  # Import the turtle graphics module

yoshi = turtle.Turtle()  # Create a new turtle object named 'yoshi'
yoshi.speed(20)  # Set the turtle's drawing speed (1 is slow, 10 is fast, 20 is very fast)

# This code uses recursion because the star function calls itself within its own definition.
# Here’s how the recursion works in your code:
# 1. Base case: The function checks if size <= 10. If this is true, the function simply returns without drawing anything, ending the recursion.
#    This is necessary to prevent an infinite loop of function calls when the star size gets too small.
# 2. Recursive case: If size > 10, the function proceeds to draw one “point” of the star (moving the turtle forward by size units, drawing one segment),
#    then calls itself again with size/2. This smaller size results in a smaller, nested star being drawn inside the current star.
#    - The line star(yoshi, size/2) is where the recursion occurs. It repeatedly calls the star function with a smaller size for each of the 5 points of the star,
#      effectively creating smaller stars within each point of the main star.
# 3. Repeating the process: The yoshi.left(216) command rotates the turtle by 216 degrees after each segment, ensuring the five points of the star are formed.
#
# Thus, recursion happens because the function star calls itself within its body, repeatedly reducing the size until it reaches the base case where no further drawing happens.
#
# In summary:
#    - The recursive function call (star(yoshi, size/2)) allows the turtle to draw smaller and smaller stars inside the main star as the size shrinks with each recursive call.

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