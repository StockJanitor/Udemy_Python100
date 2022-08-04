'''
create the screen
create and move a paddle
create another paddle
create the ball and make it move

detect collision with wall and bounce
detect collision with paddle
detect when paddle misses
keep score

'''
from ball import Ball
from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle= Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if (ball.ycor()<-275) or (ball.ycor() > 280):
        ball.y_direction *= -1
    if ((ball.xcor()>320) and (ball.distance(r_paddle)<50)) or ((ball.xcor()<-320) and (ball.distance(l_paddle)<50)):
        ball.x_direction *= -1

    if (ball.xcor()>360):
        ball.reset_position()
        ball.x_direction *= -1
        ball.y_direction *=-1
    if (ball.xcor()<-360):
        ball.reset_position()
        ball.x_direction *= -1
        ball.y_direction *=-1
screen.exitonclick()