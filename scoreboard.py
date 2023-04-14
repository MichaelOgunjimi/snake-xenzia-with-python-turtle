from turtle import Turtle

FONT = ('Arial', 15, 'italic')
ALIGNMENT = 'center'
with open("data.txt") as SCORE:
    SCORE = int(SCORE.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = SCORE
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", "w") as new_high_score:
            new_high_score.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



