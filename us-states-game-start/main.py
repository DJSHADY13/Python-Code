from math import remainder
import turtle
from matplotlib.pyplot import text
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./us-states-game-start/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title= f"Guess the state  {len(guessed_states)}/50", prompt="What's another state's name?")
    answer = answer.title()
    
    if answer == "Exit":
        remaining_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(remaining_states)
        new_data.to_csv("./us-states-game-start/states_to_learn.csv")        
        break
    if answer in all_states:
        guessed_states.append(answer)
        text = turtle.Turtle()
        text.hideturtle()
        text.color("black")
        text.penup()
        state_data = data[data.state == answer]
        text.goto(int(state_data.x),int(state_data.y))
        text.write(answer)
