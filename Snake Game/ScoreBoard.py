from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        with open("./data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0,276)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}  Highscore = {self.high_score}",False,align = "center",font=("Arial", 17, "normal"))    
    
    def score_pointed(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
        with open("data.txt",mode="w") as data:
            data.write(f"{self.high_score}")    
        self.score = 0
        self.update_scoreboard()
    