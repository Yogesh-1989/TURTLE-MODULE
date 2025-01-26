import turtle
from turtle import *

tr1 = Turtle()
tr2 = Turtle()
tr3 = Turtle()

tr1.width(4)
tr2.width(4)
tr3.width(4)

tr1.color("Purple")
tr2.color("Orange")
tr3.color("Green")

tr1.penup()
tr2.penup()
tr3.penup()

tr1.goto(-150, 150)
tr2.goto(-150, 50)
tr3.goto(-150, -50)

tr1.pendown()
tr2.pendown()
tr3.pendown()

tr1.begin_fill()
tr2.begin_fill()
tr3.begin_fill()

for i in range(3):
  tr1.forward(100)
  tr1.left(120)
  
  tr2.forward(100)
  tr2.left(120)
  
  tr3.forward(100)
  tr3.left(120)
  
tr1.end_fill()
tr2.end_fill()
tr3.end_fill()

exitonclick()
  






