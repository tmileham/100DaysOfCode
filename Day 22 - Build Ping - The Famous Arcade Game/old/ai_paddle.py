from turtle import Turtle
from random import randrange
from time import sleep

PADDLE_SPEED = 3


class Ai_Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.full_paddel = []
        self.paddel_pieces = 8
        y = 0
        for _ in range(self.paddel_pieces):
            self.paddle = Turtle()
            self.paddle.shape("square")
            self.paddle.shapesize(stretch_wid=1, stretch_len=1)
            self.paddle.penup()
            self.paddle.setheading(90)
            self.paddle.color("white")
            self.paddle.goto((620, y))
            self.full_paddel.append(self.paddle)
            y += 20

    def up(self):
        for single_part in self.full_paddel:
            single_part.setheading(90)
            single_part.forward(PADDLE_SPEED)

    def down(self):
        for single_part in self.full_paddel:
            single_part.setheading(270)
            single_part.forward(PADDLE_SPEED)