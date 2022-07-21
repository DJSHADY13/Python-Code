from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0), (-60,0)]
MOVING_FORWARD = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
     
    def __init__(self):    
        self.segments = []
        self.create_snake()
        self.body = self.segments[0]
     
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def reset(self):
        for seg in self.segments:
             seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.body = self.segments[0]
    
    def add_segment(self,position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
             
    def move(self):
        for seg_num in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.body.forward(MOVING_FORWARD)    
    
    def left(self):
        if self.body.heading() == RIGHT:
            return
        self.body.setheading(LEFT)
    
    def right(self):
        if self.body.heading() == LEFT:
            return
        self.body.setheading(RIGHT)
        
    def up(self):
        if self.body.heading() == DOWN:
            return
        self.body.setheading(UP)
        
    def down(self):
        if self.body.heading() == UP:
            return
        self.body.setheading(DOWN)
            