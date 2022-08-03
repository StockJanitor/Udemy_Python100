from turtle import Turtle

POSITION = "center"
FORMAT = ("Courier",24,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score {self.score}",align=POSITION,font=FORMAT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align=POSITION,font=FORMAT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()