from turtle import Turtle, xcor


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.displayscores()
        
        
        
    def leftscore(self):
        self.l_score += 1
        self.clear()
        self.displayscores()
        
    def rightscore(self):    
        self.r_score += 1
        self.clear()

        self.displayscores()
        
           
    def displayscores(self):
        self.goto(-120,220)
        self.write(f"{self.l_score}",False,font=("Arial", 45, "bold"))
        self.goto(120,220)
        self.write(f"{self.r_score}",False,font=("Arial", 45, "bold"))
        