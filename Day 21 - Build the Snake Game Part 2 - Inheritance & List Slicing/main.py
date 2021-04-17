from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python vs Snake")
screen.listen()
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Right", fun=snake.right)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Left", fun=snake.left)

diffculty = screen.textinput("Difficulty", "Select your difficulty (easy/hard)")

game_running = True
while game_running:
    sleep(0.1)
    screen.update()
    snake.move()

    # Detect if Snake hits food
    if snake.head.distance(food) < 15:
        food.new_location()
        scoreboard.increase_score()
        snake.extend()

    # Detect if Snake hits wall (Hard difficulty)

    if diffculty.lower() == "hard":
        if (
            snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280
        ):
            game_running = False
            scoreboard.game_over()

    # Detect if Snake hits itself

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_running = False
            scoreboard.game_over()


# Debugging purposes
# print(snake.snake[-1].xcor())
# print(snake.snake[-1].ycor())

screen.exitonclick()