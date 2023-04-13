from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collion with food.
    if snake.snake_head.distance(food) < 10:
        food.refresh()
        snake.grow()
        scoreboard.update_score()

    #Detect collion with wall.
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290 :
        game_is_on = False
        scoreboard.game_over()


    #Detect collision with tail.
    for part in snake.snake_body[1::]:
        if snake.snake_head.distance(part) < 10:
            game_is_on = False
            scoreboard.game_over()








screen.exitonclick()