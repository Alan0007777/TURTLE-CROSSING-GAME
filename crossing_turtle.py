from turtle import Turtle

class CrossingTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.seth(90)
        self.shape("turtle")
        self.color("black")
        self.speed("slowest")
        self.goto(0 , -280 )


    def move_up(self):
        self.forward(50)

    def current_position(self):
        return  self.ycor()

    def new_round(self):
        self.goto(0 , -280)


