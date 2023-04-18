import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
PADDLE_LEFT_X = -350
PADDLE_LEFT_Y = 0
PADDLE_RIGHT_X = 350
PADDLE_RIGHT_Y = 0

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # turn off animation

paddle_left = Paddle((PADDLE_LEFT_X, PADDLE_LEFT_Y))
paddle_right = Paddle((PADDLE_RIGHT_X, PADDLE_RIGHT_Y))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if Right paddle misses the ball
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()  # reset ball to center of screen, ball should start moving towards the other player
    # Detect if Left paddle misses the ball
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()






screen.exitonclick()