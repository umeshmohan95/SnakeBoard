from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scorerecord import Score
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Welcome to Snake Game')

screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

food = Food()
snake_head = snake.head
snake_head.color('blue')

score_board = Score()
game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    # game_on =  snake.move()

    # food collision
    if snake_head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score_board.game_over()

# segment collision
    for segment in snake.segments[1:]:
        if snake_head.distance(segment) < 10:
            game_on = False
            score_board.game_over()

screen.exitonclick()