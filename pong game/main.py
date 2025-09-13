import time
from turtle import Screen
from paddle import Paddle
from ball import  Ball
from scoreboard import ScoreBoard
from splitturt import MidLine

screen = Screen()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
pong = Ball()
scoreboard = ScoreBoard()
mid = MidLine()

screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
# pong.("fastest")

screen.listen()
screen.onkey(r_paddle.up_key,"Up")
screen.onkey(r_paddle.down_key,"Down")

screen.onkey(l_paddle.up_key,"w")
screen.onkey(l_paddle.down_key,"s")

game_on = True
while game_on:
    time.sleep(pong.move_speed)
    screen.update()
    pong.move()


    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()

    # DETECT COLLISION WITH PADDLE
    if (pong.distance(r_paddle) < 55 and pong.xcor() > 320) or \
            (pong.distance(l_paddle) < 55 and pong.xcor() < -320):
        pong.bounce_x()

    if pong.xcor() > 380:
        pong.reset_pos()
        scoreboard.l_point()

    if pong.xcor() < -380:
        pong.reset_pos()
        scoreboard.r_point()




screen.exitonclick()