from turtle import Turtle

FONT = ("Courier", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.draw_scoreboard(self.level)

    def draw_scoreboard(self, level):
        self.hideturtle()
        self.penup()
        self.goto(-270, 267)
        self.clear()
        self.write("Level: {0}".format(level), font=FONT)

    def next_level(self):
        self.level += 1
        self.draw_scoreboard(self.level)
