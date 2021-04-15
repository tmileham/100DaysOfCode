from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
snake = []


class Snake:
    def __init__(self):
        for position in STARTING_POSITIONS:
            snake_body = Turtle()
            snake_body.color("white")
            snake_body.shape("square")
            snake_body.penup()
            snake_body.goto(position)
            snake.append(snake_body)

    def move(self):
        for snake_body_index in range(len(snake) - 1, 0, -1):
            new_x = snake[snake_body_index - 1].xcor()
            new_y = snake[snake_body_index - 1].ycor()
            snake[snake_body_index].goto(new_x, new_y)

        if snake[0].xcor() == 300:
            snake[0].setx(-300)
        elif snake[0].xcor() == -300:
            snake[0].setx(300)
        elif snake[0].ycor() == 300:
            snake[0].sety(-300)
        elif snake[0].ycor() == -300:
            snake[0].sety(300)

        snake[0].forward(20)

    def turn_left(self):
        for segment in snake:
            segment.left(90)

    def turn_right(self):
        for segment in snake:
            segment.right(90)
