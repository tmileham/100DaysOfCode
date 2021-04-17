from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__
        self.ball = Turtle()
        self.angle = random.randint(0, 360)
        # self.angle = 180
        while self.angle > 75 and self.angle < 105:
            self.angle = random.randint(0, 360)
        self.ball.shape("circle")
        self.ball.penup()
        self.ball_speed = 5
        self.ball.color("red")
        self.ball.setheading(self.angle)

    def move(self):
        self.ball.forward(self.ball_speed)

    def bounce_x(self):
        heading = self.ball.heading()
        self.ball.setheading(180 - heading)
        self.ball_speed += 1

    def bounce_y(self):
        heading = self.ball.heading()
        self.ball.setheading(-heading)
        self.ball_speed += 1
