from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class ScoreBored(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.shapesize(10)
        self.goto(0, 270)
        self.hideturtle()
        self.updateScoreBored()

    def updateScoreBored(self):
        self.write(arg=f"Score: {self.score}",  align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)

    def point_awarded(self):
        self.clear()
        self.score += 1
        self.updateScoreBored()
