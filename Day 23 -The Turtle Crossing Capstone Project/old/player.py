from turtle import Turtle

PLAYER_MOVEMENT_SPEED = 7


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto_start()

    def goto_start(self):
        self.goto(0, -280)

    def up(self):
        self.forward(PLAYER_MOVEMENT_SPEED)

    def down(self):
        self.backward(PLAYER_MOVEMENT_SPEED)