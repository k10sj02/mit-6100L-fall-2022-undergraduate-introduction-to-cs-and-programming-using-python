import turtle
franklin = turtle.Turtle()

franklin.getscreen().bgcolor("#994444")

def star(franklin):
  for _ in range(50):
    franklin.forward(200)
    franklin.left(216)

star(franklin)

turtle.done()