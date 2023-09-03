import turtle

wind=turtle.Screen()
wind.title(" ping pong ")
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0)
#hand1
hand1=turtle.Turtle()
hand1.speed(0)
hand1.shape("square")
hand1.color("red")
hand1.shapesize(stretch_wid=5,stretch_len=1)
hand1.penup() # 3shan mayrsm4 5tot 3a 4a4a
hand1.goto(-360,0)
#hand2
hand2=turtle.Turtle()
hand2.speed(0)
hand2.shape("square")
hand2.color("blue")
hand2.shapesize(stretch_wid=5,stretch_len=1)
hand2.penup()
hand2.goto(360,0)
#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.3
ball.dy=0.3

#score
player1=0
player2=0
score=turtle.Turtle()
score.speed(0)
score.color("white") 
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player 1: 0 , player 2: 0",align="center",font=("Courier",20,"normal"))


#functions
def hand1_up():
    y = hand1.ycor()
    y+=20
    hand1.sety(y)
   
def hand1_dwon():
    y = hand1.ycor()
    y-=20
    hand1.sety(y)
   
def hand2_up():
    y = hand2.ycor()
    y+=20
    hand2.sety(y)
   
def hand2_dwon():
    y = hand2.ycor()
    y-=20
    hand2.sety(y)
   


# keyboard binding
wind.listen()
wind.onkeypress(hand1_up,"Up")
wind.onkeypress(hand1_dwon,"Down")
wind.onkeypress(hand2_up,"8")
wind.onkeypress(hand2_dwon,"2")


while True:
    wind.update()
    #move tha ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #border check
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1 #3shan terg3 ve 3ks eletegah

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1
        player1 +=1
        score.clear()
        score.write("player 1: {} , player 2: {} ".format(player1,player2),align="center",font=("Courier",20,"normal"))

    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1
        player2 +=1
        score.clear()
        score.write("player 1: {} , player 2: {} ".format(player1,player2),align="center",font=("Courier",20,"normal"))



    # tsadom ball m3 el hand
    if (ball.xcor()<360 and ball.xcor()>350) and ( ball.ycor()< hand2.ycor()+40 and ball.ycor()> hand2.ycor()-40):
        ball.setx(350)
        ball.dx *= -1
    
    if (ball.xcor()>-360 and ball.xcor()<-350) and ( ball.ycor()< hand1.ycor()+40 and ball.ycor()> hand1.ycor()-40):
        ball.setx(-350)
        ball.dx *= -1
    

