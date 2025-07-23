from turtle import Turtle , Screen
from crossing_turtle import CrossingTurtle
from cars import Cars
from round import NewRound
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("white")
screen.tracer(0)

turtle = CrossingTurtle()
car = Cars()
round = NewRound()


screen.onkey(fun= turtle.move_up ,key= "Up")
screen.listen()

crossing = True

while crossing:
    car.create()
    car.move()
    screen.update()
    time.sleep(0.1)

    for traffic in car.whole_traffic:
        if turtle.distance(traffic) < 20:
            crossing = False
            round.gameover()

    if turtle.ycor() > 280:
        turtle.new_round()
        car.new_level()
        round.new_round()

    

screen.mainloop()