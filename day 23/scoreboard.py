from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.level_update()
    
    def level_update(self):
        self.clear()
        self.goto(-380, 360)
        self.write(f"Level: {self.current_level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)

    def level_up(self):
        self.current_level += 1
        self.level_update()

