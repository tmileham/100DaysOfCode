import turtle as t
from random import choice

colors = [
    (54, 108, 149),
    (225, 201, 108),
    (134, 85, 58),
    (229, 235, 234),
    (224, 141, 62),
    (197, 144, 171),
    (143, 180, 206),
]

# Create and configure our Turtle instance
tom = t.Turtle()
tom.speed("fastest")
tom.penup()
tom.hideturtle()

# Create and configure our screen instance
screen = t.Screen()
screen.colormode(255)


def draw_circle():
    """Draw a circle on the screen"""
    circ_color = choice(colors)
    tom.fillcolor(circ_color)
    tom.color(circ_color)
    tom.pendown()
    tom.begin_fill()
    tom.circle(30)
    tom.end_fill()
    tom.penup()


# Create equal spacing between our circle
x_spacing = screen.window_width() / 10
y_spacing = screen.window_height() / 10

START_X_POS = x_pos = -435
START_Y_POS = y_pos = -390

for y in range(10):
    for x in range(10):
        tom.goto(x_pos, y_pos)
        draw_circle()
        x_pos += x_spacing
    y_pos += y_spacing
    x_pos = START_X_POS


screen.exitonclick()
