from random import randint
from turtle import Turtle


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6,stretch_wid=0.6)    
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        pos = (randint(-276,276),randint(-276,276))
        self.goto(pos) 