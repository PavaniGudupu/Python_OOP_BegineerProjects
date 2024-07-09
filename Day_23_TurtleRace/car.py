from turtle import Turtle
import random
COLORS = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']
MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random.chance = random.randint(1, 6)
        if random.
        car = self.shape('square')
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        car.goto(300, random_y)
        self.all_cars.append(car)

    def move_cars(self):
        for i in self.all_cars:
            i.backwards(MOVE_DISTANCE)
