from car import Car
from random import choice, randint
from time import sleep

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_increment = 10

    def next_level(self):
        self.cars = []
        self.move_increment *= 1.5

    def reset(self):
        for car in cars:
            car.hideturtle()
        self.cars = []

    def generate_car(self):
        random_spawn_rate = randint(1, 10)

        if random_spawn_rate > 7:
            if len(self.cars) < 25:
                y_pos = randint(-250, 250)
                car = Car(y_pos)
                self.cars.append(car)

    def destroy_car(self, index):
        del self.cars[index]

    def move(self):
        for i, car in enumerate(self.cars):
            car.move(self.move_increment)
            car.check_xpos()

            if car.check_xpos() < -330:
                self.destroy_car(i)
