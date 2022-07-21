import time
from turtle import Screen
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=600, height =600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
   

game_is_on = True
while game_is_on:
    time.sleep(0.13)
    screen.update() 
    snake.move() 
    
    #Detect collision with food and score update   
    if snake.body.distance(food) < 19:
        score.score_pointed()
        food.refresh()
        snake.extend()
    
    #Detect collison with wall
    if snake.body.xcor() > 285 or snake.body.xcor() < -285 or snake.body.ycor() > 285 or snake.body.ycor() < -285:
        
        score.reset() 
        snake.reset()
    
    #Detect collison  with tail
    for segment in snake.segments[1:]:
        if snake.body.distance(segment) < 10:
            score.reset()
            snake.reset()     
screen.exitonclick()