from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left = Paddle(-350, 0)
right = Paddle(350, 0)
ball = Ball()
scoreboard = ScoreBoard()

screen.update()

screen.listen()
screen.onkey(right.go_up, "Up")
screen.onkey(right.go_down, "Down")
screen.onkey(left.go_up, "w")
screen.onkey(left.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if (ball.distance(right) < 50 and ball.xcor() > 320) or (ball.distance(left) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()

    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()
