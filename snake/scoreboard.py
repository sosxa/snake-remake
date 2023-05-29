from turtle import Turtle
import turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(arg=(f"Score: {self.score}"), move=False, align="center", font=("Arial", 20, "normal"))
        self.hideturtle()

    def increase(self):
        self.score +=1
        self.clear()
        self.write(arg=(f"Score: {self.score}"), move=False, align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(arg=("Game Over"), move=False, align="center", font=("Arial", 20, "normal"))
        self.hideturtle()