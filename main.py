import time
from turtle import Screen
from car_manager import *
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
traffic = 10
count = 1
player = Player()

screen.listen()

screen.onkey(player.move_forward, 'Up')
screen.onkey(player.move_backward, 'Down')
list_cars = []
scoreboard = Scoreboard()
game_is_on = True
sleep = 0.1


while game_is_on:

    if count % traffic == 0:
        car = CarManager()
        list_cars.append(car)
    for car in list_cars:
        car.move()
        if player.distance(car) < 22:
            game_is_on = False
    time.sleep(sleep)
    screen.update()
    count += 1

    if player.ycor() > 280:
        player.starting_position()
        traffic -= 2
        sleep *= 0.95
        scoreboard.level_up()

screen.exitonclick()