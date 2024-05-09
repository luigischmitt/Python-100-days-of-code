import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")

image = "Python-100-days-of-code/day 25/US States Game/blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)

turtle.shape(image)

df = pd.read_csv("Python-100-days-of-code/day 25/US States Game/50_states.csv")
states_list = df["state"].to_list()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

guessed_states = []
score = 0

while len(guessed_states) <= 50:
    if answer_state in states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align="center",font=("Arial", 8, "normal"))
        score += 1
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    elif answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    else:
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    
screen.exitonclick()
