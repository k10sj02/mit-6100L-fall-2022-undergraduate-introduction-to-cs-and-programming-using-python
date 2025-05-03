# def main():
#   print_column(3)

# def print_column(height):
#   for _ in range(height):
#     print("#")

# main()

# def main():
#   print_row(4)

# def print_row(width):
#   print("?" * width)

# main()

# Define the main function
def main():
  # Call the function to print a square of size 3
  print_square(3)

# Define a function that prints a square of "#" characters
def print_square(size):
  # Loop through each row
  for i in range(size):
    # Loop through each column in the current row
    for j in range(size):
      # Print "#" without moving to a new line
      print("#", end="")
    # After printing one full row, move to the next line
    print()

# Call the main function to run the program
main()