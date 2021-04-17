from turtle import Turtle


class Net:
    def __init__(self):
        super().__init__
        y_pos = 330
        for _ in range(22):
            self.net = Turtle()
            self.net.shape("square")
            self.net.color("white")
            self.net.shapesize(stretch_len=0.8, stretch_wid=0.2)
            self.net.penup()
            self.net.setheading(90)
            self.net.goto((0, y_pos))
            y_pos -= 31