import sys 

# ATTEMPT 1 

# if len(sys.argv) < 2:
#   print("Too few arguments")
# elif len(sys.argv) > 2:
#   print("Too many arguments")
# else:
#   print("hello, my name is", sys.argv[1])

# ATTEMPT 2 (more elegant)
# # Check for errors
# if len(sys.argv) < 2:
#   sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#   sys.exit("Too many arguments")

# # Print name tags
#   print("hello, my name is", sys.argv[1])

# ATTEMPT 3 (even more elegant)

if len(sys.argv) < 2:
  sys.exit("Too few arguments")

# Print name tags
for arg in sys.argv[1:]:
  print("hello, my name is", arg)