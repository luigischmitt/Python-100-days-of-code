# HURDLE 3 AT (https://reeborg.ca/reeborg.html)

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    if wall_in_front() is True:
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    elif front_is_clear() is True:
        move()

while not at_goal():
    jump()