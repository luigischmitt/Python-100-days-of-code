import turtle as t
import random

ayres = t.Turtle()
t.colormode(255)
ayres.pensize(15)
ayres.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

direction = [0, 90, 180, 270]

for _ in range(200):
    rgb = random_color()
    ayres.forward(40)
    ayres.pencolor(rgb)
    ayres.setheading(random.choice(direction))

screen = t.Screen()
screen.exitonclick()
