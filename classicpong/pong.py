import turtle, os

#Display 

sc = turtle.Screen()
sc.title("Pong by Mike")
sc.setup(width=800, height=600)
sc.bgcolor('black')
sc.tracer(0)


#Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color('white')
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color('white')
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.color('white')
ball.shape('square')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.08
ball.dy = 0.08

#Score board

sb = turtle.Turtle()
sb.speed(0)
sb.color('white')
sb.penup()
sb.hideturtle()
sb.goto(0, 260)
sb.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Scores

score_a = 0
score_b = 0



#Function that move the Paddles

def move_paddle_a_up():
    #move paddle a up 
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def move_paddle_a_down():
    #move paddle a down
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def move_paddle_b_up():
    #move paddle b up
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def move_paddle_b_down():
    #move paddle b down
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



sc.listen()
sc.onkeypress(move_paddle_a_up, 'w')
sc.onkeypress(move_paddle_a_down, 's')
sc.onkeypress(move_paddle_b_up, 'a')
sc.onkeypress(move_paddle_b_down, 'd')



#main loop 
while True:
    sc.update()

    #Make the ball move

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Make the ball bounce of Y edges

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay click.mp3")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay click.mp3")

    #Make the ball go back to the center if it's gone far beyond X edges

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        sb.clear()
        sb.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        sb.clear()
        sb.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


    #Make the ball bounce off the paddles

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50:
        ball.setx(-340)
        ball.dx *= -1

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50:
        ball.setx(340)
        ball.dx *= -1

    