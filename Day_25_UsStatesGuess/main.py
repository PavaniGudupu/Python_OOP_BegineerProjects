from turtle import Turtle, Screen
import pandas as pd

FONT = ('Courier', 24, 'normal')

screen = Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)


turtle = Turtle()
turtle.shape(image)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name: ").title()

    print(answer_state)
    guessed_states.append(answer_state)
    
    if answer_state == "Exit":
            missing_states = []
            for state in all_states:
                if state not in guessed_states:
                      missing_states.append(state)
            new_data = pd.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break

    if answer_state in all_states:
            turtle.hideturtle()
            turtle.penup()
            state_data = data[data.state == answer_state]
            turtle.goto(state_data.x.item(), state_data.y.item())
            turtle.write(answer_state)




screen.exitonclick()