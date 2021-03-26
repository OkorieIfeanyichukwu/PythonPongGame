import turtle #turtle is the module used for graphics,mainly for simple games.For complex games you use pygame
import winsound #this module helps add sound in the game for windows,but you will need to add the sound file
#import os is for mac. You can download sounds from Freesound.com,incompetech and Open Art Game
win=turtle.Screen()
win.title("pong by Light")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)# it stops the turtle graphics window from automatically updating,so you have to manually update and it makes the game run faster
winsound.PlaySound("long.wav",winsound.SND_ASYNC)

#score
score_L=0
score_R=0

#right_paddle
right_paddle=turtle.Turtle() #small t turtle for module name and capital T Turlt() for the class name
right_paddle.speed(0) #speed of animation
right_paddle.shape("square")
right_paddle.shapesize(stretch_len=1,stretch_wid=5)
right_paddle.color("white")
right_paddle.penup() #this avoids drawing line as we move around because that is what turtle does.
#remember that python runs line by line so penup() should always be before the goto()
right_paddle.goto(350,0) 


#left_paddle
left_paddle=turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.shapesize(stretch_len=1,stretch_wid=5)
left_paddle.color("white")
left_paddle.penup() 
left_paddle.goto(-350,0)


#ball
ball=turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.penup()
ball.goto(0,0)
#set the ball movement in both x and y direction
ball.dx=0.2 #this means that everytime the ball moves, it moves by 2pixels
ball.dy=0.2

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("white")
pen.hideturtle() #we dont want to see the turtle,we just want to see what it writes out
pen.goto(0,250)
pen.write("Player L:0 Player R:0",align="center",font=("courier",24,"italic"))

#function
def right_paddle_up():
    y=right_paddle.ycor()
    y+=20
    right_paddle.sety(y)

def right_paddle_down():
    y=right_paddle.ycor()
    y-=20
    right_paddle.sety(y)

def left_paddle_up():
    y=left_paddle.ycor()
    y+=20
    left_paddle.sety(y)

def left_paddle_down():
    y=left_paddle.ycor()
    y-=20
    left_paddle.sety(y)

#keyboard input
win.listen()
win.onkeypress(right_paddle_up,"Up")
win.onkeypress(right_paddle_down,"Down")
win.onkeypress(left_paddle_up,"w") #when i put lower case u in Up and lower case D in down,the graphic window stoped
#showing,as if the win.update() is no longer functioning. This occurs when there is an error
win.onkeypress(left_paddle_down,"s")


#main game loop
while True:
    win.update() #This is what keeps the window graphic of the turtle module on and steady

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1

   # if ball.xcor()>390:
     #   ball.setx(390)
     #   ball.dx *= -1
   # if ball.xcor()<-390:
      #  ball.setx(-390)
      #  ball.dx *= -1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        score_L += 1
        #we update the score on the screen using format method,but before we update,we have to clear the initial
        #else the turtl will be writing on top of initial scores
        pen.clear()
        pen.write("Player L:{} Player R:{}".format(score_L,score_R),align="center",font=("courier",24,"italic"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_R += 1
        pen.clear()
        pen.write("Player L:{} Player R:{}".format(score_L,score_R),align="center",font=("courier",24,"italic"))

    #paddle and ball collision
    if ball.xcor() >340 and (ball.ycor()<right_paddle.ycor()+50 and ball.ycor()>right_paddle.ycor()-50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("sound/KickPunchy.wav",winsound.SND_ASYNC) #if the sound is Asynchronous it will play the sound
        #on the background,if it is not asynchronous program will stop
    if ball.xcor() <-340 and (ball.ycor()<left_paddle.ycor()+50 and ball.ycor()>left_paddle.ycor()-50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("sound/kickpunchy.wav",winsound.SND_ASYNC)


    