import turtle
yoshi = turtle.Turtle()

yoshi.speed(20)

def star(yoshi, size):
  if size <= 10:
    return
  else:
    for _ in range(5):
      yoshi.forward(size)
      star(yoshi, size/2)
      yoshi.left(216)

star(yoshi, 365)

turtle.done()