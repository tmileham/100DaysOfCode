# from turtle import Turtle, Screen, colormode
from random import choice, randint
from turtle import Turtle, Screen, colormode


# Create a Turtle object named 'Tom
tom = Turtle()

tom.shape("turtle")
tom.width(1)
tom.speed("fastest")

# Adjust Turtle module colormode to RGB 255
colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


for angle in range(0, 360, 5):
    tom.setheading(angle)
    tom.color(random_color())
    tom.circle(100)


screen = Screen()
screen.exitonclick()