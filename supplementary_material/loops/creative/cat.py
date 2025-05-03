# #Run from the CLI using the command: python cat.py 

# while True:
#   n = int(input("What's n? "))
#   if n > 0:
#       break

# for _ in range(n):
#   print("meow")

def main():
  number = get_number()
  meow(number)

def get_number():
  while True:
    n = int(input("What's n? "))
    if n > 0:
      break
  return n

def meow(n):
  for _ in range(n):
    print("meow")

if __name__ == "__main__":
    main()