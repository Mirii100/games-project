import  turtle
import winsound # adds sound to the game
wn=turtle.Screen()
wn.title('intro to gaming  ')
wn.bgcolor('green')
wn.setup(width=800,height=600) #this sets size of screen
wn.tracer(0)
# score track
score_a=0
score_b=0


# we need players in a game ,then lets  call them ply a,b ..
player_a=turtle.Turtle()
player_a.speed(0)
player_a.shape('square')
player_a.color('white')
player_a.shapesize(stretch_wid=5,stretch_len=1)
player_a.penup()
player_a.goto(-350,0)

player_b=turtle.Turtle()
player_b.speed(0)
player_b.shape('square')
player_b.color('white')
player_b.shapesize(stretch_wid=5,stretch_len=1)
player_b.penup()
player_b.goto(+350,0)
# ball for playing
ball=turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('blue')

ball.penup()
ball.goto(0,0)
ball.dx=1
ball.dy=-1
# lets create a score by use of pen
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('player A    player B : ',align='center',font=('courier',24,'normal'))


# functions to move players
def player_a_up():
    y=player_a.ycor()
    y+=20
    player_a.sety(y)

def player_b_up():
    y=player_b.ycor()
    y+=20
    player_b.sety(y)


def player_a_down():
    y=player_a.ycor()
    y-=20
    player_a.sety(y)


def player_b_down():
    y=player_b.ycor()
    y-=20
    player_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(player_a_up,'q')
wn.onkeypress(player_a_down,'a')
wn.onkeypress(player_b_up,'Up')
wn.onkeypress(player_b_down,'Down')
# main game loop
while True:
    wn.update()
    # make the ball move
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    # border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1
        winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)


    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *=-1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a +=1
        pen.clear() # clears  the screen before anything else is added
        pen.write('player A :{}  player B : {}'.format(score_a,score_b), align='center', font=('courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write('player A :{}  player B : {}'.format(score_a,score_b), align='center', font=('courier', 24, 'normal'))

    # paddle collision
    if ball.xcor()>340and ball.xcor()<350 and (ball.ycor()<player_b.ycor()+40 and ball.ycor()>player_b.ycor()-40):
        ball.setx(340)
        ball.dx*=-1

    if ball.xcor()<-340and ball.xcor()>-350 and (ball.ycor()<player_a.ycor()+40 and ball.ycor()>player_a.ycor()-40):
        # you can change direction  in setx by inerting a - sign infront of the value  in our case its 340
        ball.setx(-340)
        ball.dx*=-1