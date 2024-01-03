import random
import turtle
import time


turtle = turtle
turtle.speed(1000)

circle_amount = 8
circle_size = 100
colors = ["orange","blue","white","pink"]

turtle.dot(5000)
color_pick = random.choice(colors)

for i in range(300):
  turtle.color(color_pick)
  turtle.circle(circle_size)
  turtle.lt(45)
  circle_amount -= 1
  if circle_amount == 0:
   color_pick = random.choice(colors)
   circle_size = circle_size - 5
   circle_amount = 8
   
time.sleep(100)
