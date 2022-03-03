from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(330, 150)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))


    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over!', align="center", font=("Courier", 50, "normal"))
