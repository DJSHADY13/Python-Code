import random
from turtle import Turtle, Screen, color

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bets",prompt="Which turtle will win the race: ")

colors = ["red", "yellow", "green", "blue", "purple", "orange"]
y_axis = [-100, -70, -40, -10, 20, 50]
all_turtles = []

for turtle_times in range(0,6):    
    tim = Turtle("turtle")
    tim.penup()
    tim.color(colors[turtle_times])
    tim.goto(x=-235,y=y_axis[turtle_times])
    all_turtles.append(tim)
    
    
if bet:
    is_race_on = True 

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if bet == turtle.pencolor():
                print("You won")
            else:
                print("You lost")
            print(turtle.pencolor())        
            is_race_on = False
            break;        
        
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
    
screen.exitonclick()