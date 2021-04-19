from turtle import Turtle
from random import choice


colors = ("red", "orange", "blue", "green")

STARTING_X_POSITION = 300


class Car(Turtle):
    def __init__(self, y_position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(choice(colors))
        self.goto(STARTING_X_POSITION, y_position)
        self.setheading(180)
        self.shapesize(stretch_len=2, stretch_wid=1)

    def move(self, movement_speed):
        self.forward(movement_speed)

    def check_xpos(self):
        return self.xcor()
