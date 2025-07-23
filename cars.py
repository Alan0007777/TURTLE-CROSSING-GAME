from turtle import Turtle
from random import choice, randint

COLORS = ["blue" , "green" , "black" , "yellow"]
INITIAL_SPEED = 10
INCREMENT_SPEED = 5

class Cars:
    def __init__(self):
        self.movespeed = INITIAL_SPEED
        self.whole_traffic = []

    def create(self):
        generation = randint(1,4)
        if generation == 4:
            t = Turtle()
            t.shape("square")
            t.shapesize(1,2)
            t.penup()
            t.color(choice(COLORS))
            t.goto(400 , randint(-250, 250 ))
            self.whole_traffic.append(t)

    def move(self):
        for car in self.whole_traffic:
            car.backward(self.movespeed)

    def new_level(self):
        
        self.movespeed += INCREMENT_SPEED



    








        


           
       














