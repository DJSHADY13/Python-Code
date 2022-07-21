from turtle import Screen, Turtle
from Paddle import Paddle
from Ball import Ball
from Score import Score
import time
speed = 0.07

#Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()

#Paddle Movement capture    
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

is_on = True

while is_on:
    time.sleep(speed)
    screen.update()
    ball.move()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.hit()
        speed -= 0.0006
        
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.hit()
        speed -= 0.0006
        
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        
    if ball.xcor() > 380:
        speed = 0.07
        ball.reset()
        score.leftscore()
        
    if ball.xcor() < -380:
        speed = 0.07
        ball.reset()  
        score.rightscore()
             
screen.exitonclick()