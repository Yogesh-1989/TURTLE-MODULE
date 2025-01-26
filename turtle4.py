import turtle
from turtle import *

def square(t, size):
  for i in range(4):
    t.forward(size)
    t.left(90)
    
def triangle(t, size):
  for i in range(3):
    t.forward(size)
    t.left(120)
    
t = Turtle()

square(t, 75)

triangle(t, 120)
