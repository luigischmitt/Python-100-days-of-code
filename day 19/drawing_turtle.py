from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")
screen = Screen()

def move_backwards():
    tim.backward(10)

def move_forwards():
    tim.forward(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def clear_screen():
    tim.reset() # Reset everything
    tim.color("green") # The function "reset()" will reset the turtle to black color, so we need to do this

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
