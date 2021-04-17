from turtle import Screen
from paddle import Paddle
from ai_paddle import Ai_Paddle
from net import Net
from ball import Ball
from time import sleep


# from time import sleep


screen = Screen()

screen.setup(width=1280, height=720)
screen.bgcolor("black")
screen.title("Poooooooooong!!!")
screen.tracer(0)

screen.listen()

player = Paddle()
ai = Ai_Paddle()

net = Net()
ball = Ball()

screen.onkeypress(key="Up", fun=player.up)
screen.onkeypress(key="Down", fun=player.down)

screen.onkeypress(key="g", fun=ball.bounce_x)
screen.onkeypress(key="h", fun=ball.bounce_y)

game_running = True

while game_running:
    sleep(0.01)
    ball.move()

    # Detect if the ball hits the top and bottom wall
    if ball.ball.ycor() > 340 or ball.ball.ycor() < -340:
        ball.bounce_y()

    # Detect if the ball hits the Player Paddle
    for single_part in player.full_paddel:
        if single_part.distance(ball.ball) < 20:
            ball.bounce_x()

    for single_part in ai.full_paddel:
        if single_part.distance(ball.ball) < 20:
            ball.bounce_x()

    if single_part.ycor() > 360:
        ai.up()
        break
    elif single_part.ycor() < -360:
        ai.down()
        break

    screen.update()


screen.exitonclick()