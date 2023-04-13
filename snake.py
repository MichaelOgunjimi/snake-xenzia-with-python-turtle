from turtle import Turtle
BODY_POSITIONS = [(0, 0), (-10, 0), (-20, 0), (-30, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.body_position = BODY_POSITIONS
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        for position in self.body_position:
            self.add_part(position)


    def add_part(self, position):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.shapesize(0.5)
        new_part.penup()
        new_part.goto(position)
        self.snake_body.append(new_part)


    def grow(self,):
        """extends the length of the snake as it consumes foods """
        self.add_part(self.snake_body[-1].position())


    def move(self):
        for part_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[part_num - 1].xcor()
            new_y = self.snake_body[part_num - 1].ycor()
            self.snake_body[part_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)