from turtle import Turtle

STARTING_POSITION = (0, -380)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 380

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

