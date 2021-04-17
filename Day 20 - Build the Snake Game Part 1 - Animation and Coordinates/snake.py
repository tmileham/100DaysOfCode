from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_body = Turtle()
            snake_body.color("white")
            snake_body.shape("square")
            snake_body.penup()
            snake_body.goto(position)
            self.snake.append(snake_body)

    def move(self):
        for snake_body_index in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_body_index - 1].xcor()
            new_y = self.snake[snake_body_index - 1].ycor()
            self.snake[snake_body_index].goto(new_x, new_y)

        # Snake can travel through walls.. for now
        if self.head.xcor() == 300:
            self.head.setx(-300)
        elif self.head.xcor() == -300:
            self.head.setx(300)
        elif self.head.ycor() == 300:
            self.head.sety(-300)
        elif self.head.ycor() == -300:
            self.head.sety(300)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
