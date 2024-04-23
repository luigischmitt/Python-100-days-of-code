from turtle import Turtle
# Some constants: 
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    segments = []

    def __init__(self):
        position_x = [0, -20, -40]
        for i in range (0, 3):
            self.new_segment = Turtle("square")
            self.new_segment.color("white")
            self.new_segment.penup()
            self.new_segment.setposition(position_x[i], 0)
            self.segments.append(self.new_segment)
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(2, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y) 
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


