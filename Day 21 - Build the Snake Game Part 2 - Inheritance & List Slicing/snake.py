from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segment = []
        self.movement_speed = 20
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        """ Creates our starting snake """
        for position in STARTING_POSITIONS:
            snake_body = self.body_shape(position)
            self.segment.append(snake_body)

    def body_shape(self, position):
        """Function which creates the body shape for our snake.
        Returns this customised Turtle object"""
        snake_body_part = Turtle()
        snake_body_part.color("white")
        snake_body_part.shape("square")
        snake_body_part.penup()
        snake_body_part.goto(position)
        return snake_body_part

    def extend(self):
        snake_body = self.body_shape(self.segment[-1].position())
        self.segment.append(snake_body)

    def move(self):
        for snake_body_index in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[snake_body_index - 1].xcor()
            new_y = self.segment[snake_body_index - 1].ycor()
            self.segment[snake_body_index].goto(new_x, new_y)

        # Snake can travel through walls.. for now
        print(f"X: {self.head.xcor()}")
        print(f"Y: {self.head.ycor()}")

        if self.head.xcor() > 300:
            self.head.setx(-300)
        elif self.head.xcor() < -300:
            self.head.setx(300)
        elif self.head.ycor() > 300:
            self.head.sety(-300)
        elif self.head.ycor() < -300:
            self.head.sety(300)

        self.head.forward(self.movement_speed)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
