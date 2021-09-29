from turtle import Screen, Turtle
from snake import Snake
import time
screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor('red')
screen.title("Welcome my Snake Game")
screen.tracer(0)

snake =  Snake()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    snake.move()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.exitonclick()