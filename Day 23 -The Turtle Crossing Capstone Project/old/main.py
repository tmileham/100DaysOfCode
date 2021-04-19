from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car import Car
from car_manager import CarManager
from time import sleep
from random import randrange

# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Create Player Object
car_manager = CarManager()


# Scoreboard
scoreboard = Scoreboard()

# Game Loop
def start():
    player = Player()

    # Player Behaviour
    screen.onkeypress(fun=player.up, key="Up")
    screen.onkeypress(fun=player.down, key="Down")

    game_running = True
    while game_running:
        car_manager.generate_car()

        car_manager.move()

        sleep(0.1)
        screen.update()

        # Player reached the other side
        if player.ycor() > 305:
            car_manager.next_level()
            screen.reset()
            scoreboard.next_level()
            start()


start()


# TODO:
# DONE: Create Player Behaviour
# DONE: Create Car objects
# DONE: Create Car Behaviour
# DONE: Create gameplay loop
# Detect collision with car
# Create Scoreboard object
# Update scoreboard, adjust difficulty and reset game


screen.exitonclick()