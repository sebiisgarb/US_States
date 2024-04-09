import pandas
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_to_learn = []

states = pandas.read_csv("50_states.csv")

all_states = states.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="Guess a state:").title()

    if answer_state == "Exit":
        for state in all_states:
            if state in guessed_states:
                continue
            else:
                states_to_learn.append(state)
        pandas.Series(states_to_learn).to_csv("States_to_learn.csv")
        break
    if answer_state in all_states:
        t = Turtle()
        t.penup()
        t.hideturtle()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state, align="center")
        guessed_states.append(answer_state)
