from turtle import Turtle, Screen
import random

ayres = Turtle()
ayres.shape("turtle")

colors = ["blue", "green", "yellow", "black", "red", "purple", "cyan", "orange", "saddle brown"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        ayres.forward(100)
        ayres.right(angle)

for shape_side in range(3, 11):
    ayres.color(random.choice(colors))
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()
