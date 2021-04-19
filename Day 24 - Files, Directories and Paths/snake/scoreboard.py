from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(
            "Day 24 - Files, Directories and Paths\snake\data.txt", mode="r"
        ) as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 268)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} - High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(
                "Day 24 - Files, Directories and Paths\snake\data.txt", mode="w"
            ) as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
