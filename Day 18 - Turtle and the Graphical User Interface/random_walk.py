# from turtle import Turtle, Screen, colormode
from random import choice, randint
from turtle import Turtle, Screen, colormode


# Create a Turtle object named 'Tom
tom = Turtle()

tom.shape("turtle")
tom.color("green")
tom.width(8)
tom.speed("fastest")

# Adjust Turtle module colormode to RGB 255
colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def random_heading_and_colour():
    degrees = [0, 90, 180, 270]
    tom.setheading(choice(degrees))
    tom.color(random_color())


for _ in range(300):
    random_heading_and_colour()
    tom.forward(25)


screen = Screen()
screen.exitonclick()
