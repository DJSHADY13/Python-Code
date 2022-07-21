from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.xmove = 10
        self.ymove = 10
        self.firstmove()
        
    def firstmove(self):
        self.goto(self.xcor(),self.ycor() + 30)    
    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)
    
    def bounce(self):
        self.ymove *= -1  
    
    def hit(self):
        self.xmove *= -1  
    
    def reset(self):
       self.goto(0,0)       