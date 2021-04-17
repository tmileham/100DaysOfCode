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

screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Right", fun=snake.right)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Left", fun=snake.left)


screen.update()
game_running = True
while game_running:
    sleep(0.1)
    screen.update()
    snake.move()


screen.exitonclick()