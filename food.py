from turtle import Turtle
import random

POSITION = (random.randint(-280, 280), random.randint(-280, 280))
COLOR = ['Red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.refresh()
        self.shapesize(0.5)
        self.color(random.choice(COLOR))
        self.speed("fastest")

    def refresh(self):
        self.color(random.choice(COLOR))
        self.goto(POSITION)
