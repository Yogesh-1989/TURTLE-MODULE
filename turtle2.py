from turtle import *

tur = Turtle()
tur.width(7)
tur.color("orange")

for i in range(6):
  tur.forward(100)
  tur.right(60)
  tur.backward(10)
  tur.back(15)
  
print("Wow what a beautiful hexagon.!")
  
  
exitonclick()