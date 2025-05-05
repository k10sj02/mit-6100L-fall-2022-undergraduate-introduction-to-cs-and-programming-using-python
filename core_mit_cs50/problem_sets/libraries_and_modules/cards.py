# import random

# cards = ["jack", "queen", "king"]

# def main():
#   print(random.sample(cards, k=2)) #sampling without replacements makes sure that each returned value is unique

# main()


import random

cards = ["jack", "queen", "king"]

def main():
  random.seed(0)
  print(random.choices(cards, weights=[75, 20, 5], k=2))

main()