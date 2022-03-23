import time
from snake import Snake
from food import Food
from scorebored import ScoreBored
from turtle import Screen

SPEED = 0.09
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title('Snake')
s.tracer(0)
scorebored = ScoreBored()
snake = Snake()
food = Food()
s.listen()
s.onkey(snake.up, 'Up')
s.onkey(snake.down, 'Down')
s.onkey(snake.left, 'Left')
s.onkey(snake.right, 'Right')
running = True
while running:
    s.update()
    time.sleep(SPEED)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorebored.point_awarded()

    for segs in snake.segments[1:]:
        if snake.head.distance(segs) < 10:
            running = False
            scorebored.game_over()

s.exitonclick()
