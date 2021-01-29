from random import randint, choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.penup()
        self.shape('square')
        self.shapesize(1, 2)
        self.color(choice(COLORS))
        self.setheading(180)
        self.goto(300, randint(-250, 280))
        self.speed = (randint(1, 10))

    def move(self):
        self.forward(self.speed)

    # def move(self):
