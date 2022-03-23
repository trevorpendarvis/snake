from turtle import Turtle

DISTANCE_MOVED = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def add_segment(self, pos):
        t = Turtle("square")
        t.speed("fastest")
        t.color("white")
        t.penup()
        t.goto(pos)
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        rightWall = (self.head.xcor() >= 270 and self.head.heading() == RIGHT)
        leftWall = (self.head.xcor() <= -270 and self.head.heading() == LEFT)
        upWall = (self.head.ycor() >= 270 and self.head.heading() == UP)
        downWall = (self.head.ycor() <= -270 and self.head.heading() == DOWN)
        if not (rightWall or leftWall or upWall or downWall):
            for seg_num in range(len(self.segments) - 1, 0, -1):
                x = self.segments[seg_num - 1].xcor()
                y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(x, y)
            self.segments[0].forward(DISTANCE_MOVED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
