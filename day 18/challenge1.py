from turtle import Turtle, Screen

ayres = Turtle()
ayres.shape("turtle")

for _ in range(25):
    ayres.pendown()
    ayres.forward(10)
    ayres.penup()
    ayres.forward(10)

screen = Screen()
screen.exitonclick()
