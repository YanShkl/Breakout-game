from turtle import Screen, tracer
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Target



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -270))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

# Data variables
targets = []
tx, ty = -250, 260
data = 0
game_is_on = True

def create_blocks():
    global tx,ty
    tracer(0)
    for _ in range(5):
        for _ in range(10):
            target = Target(tx, ty)
            targets.append(target)
            tx += 55
        ty -= 25
        tx = -250
    tracer(1)

#Create Initial bricks
create_blocks()



while game_is_on:
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    #Detect collision with ceiling
    if ball.ycor() > 280 and ball.y_move > 0:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(paddle) < 40 and ball.xcor() > -320 and ball.y_move < 0:
        ball.bounce_y()


    #Detect R paddle misses
    if ball.ycor() < -400:
        scoreboard.game_over()

    #Detect collision with block
    if ball.ycor() >= 135:
        for target in targets:
            if not target.white:
                if ball.ycor() >= target.ycor() - 25:
                    if ball.xcor() >= target.xcor() - 25:
                        if ball.xcor() <= target.xcor() + 25:
                            ball.bounce_y()
                            target.color('black')
                            target.white = True
                            scoreboard.r_point()
                            data += 1
                            # Detect destructing all bricks
                            if data == 50:
                                create_blocks()
                                data = 0
                            break




screen.exitonclick()