import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=800)
screen.title("Crossing Road Turtle")
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect colission with car.
    for i in range(len(car_manager.all_cars)):
        if turtle.distance(car_manager.all_cars[i]) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing.
    if turtle.ycor() >= 380:
        scoreboard.level_up()
        turtle.goto(0, -380)
        car_manager.increase_speed()


screen.exitonclick()
