from turtle import Turtle

class NewRound(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-350 , 260 )
        self.write(f"LEVEL : {self.lvl}" , move=False, align="left", font=("Arial", 20, "normal"))

    def new_round(self):
        self.lvl += 1
        self.clear()
        self.write(f"LEVEL : {self.lvl}" , move=False, align="left", font=("Arial", 20, "normal"))

    def gameover(self):
        t = Turtle()
        t.penup()
        t.hideturtle()
        t.color("black")
        t.color("black")
        t.goto(0 , 0 )
        t.write("GAME OVER" , move=False, align="center", font=("Arial", 20, "normal"))
        