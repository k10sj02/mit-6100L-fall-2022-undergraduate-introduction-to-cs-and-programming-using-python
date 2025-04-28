import turtle

bob = turtle.Turtle()
bob.speed(20)

bob.color("red", "yellow")

bob.begin_fill()
for _ in range(250):
  bob.forward(400)
  bob.left(210)

bob.end_fill()

turtle.done()
