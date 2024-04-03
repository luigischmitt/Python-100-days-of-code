# ROBOT MAZE AT (https://reeborg.ca/reeborg.html)

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif right_is_clear() is False:
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_left()
        move()