import turtle as t

ayres = t.Turtle()
ayres.shape("turtle")
ayres.color("green")
ayres.speed("fastest")

for i in range(200):
    ayres.circle(100)
    ayres.setheading(ayres.heading() + i)

screen = t.Screen()
screen.exitonclick()
