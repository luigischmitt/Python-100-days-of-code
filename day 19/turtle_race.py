# THE TURTLE RACE

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1000, height=600)
bet = screen.textinput("Make a bet", "Who will win the race? Enter a colour:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-250, -150, -50, 50, 150, 250]
all_turtles = []

# Creating the turtles:
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-450, y=y_pos[i])
    all_turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 480:
            winner = turtle.pencolor()
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

if winner == bet:
    print(f"You win! The {winner} turtle won the race.")
else:
    print(f"You lose! The {winner} turtle won the race.")

screen.exitonclick()
