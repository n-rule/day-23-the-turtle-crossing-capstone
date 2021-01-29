FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.refresh_scoreboard()

    def level_up(self):
        self.level += 1
        self.clear()
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.write(f'Level : {self.level}', False, align='center', font=FONT)