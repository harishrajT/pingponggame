from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with top,bottom wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >325 or ball.distance(l_paddle) < 50 and ball.xcor() < - 325 :
        ball.bounce_x()

    #right paddle miss the ball
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()

    # right paddle miss the ball
    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()