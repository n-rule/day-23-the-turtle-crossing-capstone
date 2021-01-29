from turtle import Turtle
from random import randint, choice

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

    def move(self):
        self.forward(randint(1, 7))

    # def move(self):
