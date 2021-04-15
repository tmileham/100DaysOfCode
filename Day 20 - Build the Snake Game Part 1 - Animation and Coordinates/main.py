from snake import Snake
from turtle import Screen
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python vs Snake")
screen.listen()
screen.tracer(0)

snake = Snake()

screen.onkeypress(key="a", fun=snake.turn_left)
screen.onkeypress(key="d", fun=snake.turn_right)

screen.update()
game_running = True
while game_running:
    sleep(0.1)
    screen.update()
    snake.move()


screen.exitonclick()