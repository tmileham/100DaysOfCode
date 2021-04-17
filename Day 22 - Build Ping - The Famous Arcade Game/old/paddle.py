from turtle import Turtle

PADDLE_SPEED = 30


class Paddle(Turtle):
    def __init__(self, players=1):
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
            if players == 1:
                self.paddle.goto((-618, y))
            elif players == 2:
                self.paddle.goto((618, y))
            self.full_paddel.append(self.paddle)
            y += 20

    def up(self):
        for single_part in self.full_paddel:
            # if single_part.ycor() < (360 - 2 * self.paddel_pieces):
            single_part.setheading(90)
            single_part.forward(PADDLE_SPEED)

    def down(self):
        for single_part in self.full_paddel:
            # if single_part.ycor() > (-360 + 2 * self.paddel_pieces):
            single_part.setheading(270)
            single_part.forward(PADDLE_SPEED)
