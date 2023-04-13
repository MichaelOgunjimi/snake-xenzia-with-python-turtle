from turtle import Turtle
FONT = ('Arial', 15, 'italic')
ALIGNMENT = 'center'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT )
        self.speed("fastest")

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


