from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.currentscore = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 278)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.scoretext = "{0}{1}".format("Score: ", self.currentscore)
        self.write(self.scoretext, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.currentscore += 1
        self.clear()
        self.update_scoreboard()
