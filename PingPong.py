import turtle


#The Screen
window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800,height=400)
window.tracer(0)

#Enter Player Names And Maximum Score Attainable
Player_1_name = turtle.textinput("Player 1", "Enter your name")
Player_2_name = turtle.textinput("Player 2", "Enter your name")
count = 0
max_score = 0
while max_score < 1:
    if count < 1:
        max_score = turtle.numinput("Goal","Enter the goal")
    else :
        max_score = turtle.numinput("Goal","Invalid input. Goal should be greater than 0. Please enter a valid goal")
    count+=1

#Score
#Initial score set to 0
Player_1_score = 0
Player_2_score = 0

#Player 1 
Player_1 = turtle.Turtle()
Player_1.speed(0)
Player_1.shape("square")
Player_1.color("red")
Player_1.penup()
Player_1.goto(-350,0)
Player_1.shapesize(stretch_wid=5,stretch_len=1)


#Player 2 
Player_2 = turtle.Turtle()
Player_2.speed(0)
Player_2.shape("square")
Player_2.color("blue")
Player_2.penup()
Player_2.goto(350,0)
Player_2.shapesize(stretch_wid=5,stretch_len=1)


#The Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.dx = 0.07
Ball.dy = 0.07


#Pen
Pen = turtle.Turtle()
Pen.speed(0)
Pen.color("white")
Pen.penup()
Pen.hideturtle()
Pen.goto(0,160)
Pen.write("{}: 0  {}: 0".format(Player_1_name,Player_2_name),align="center",font=("courier",24,"normal"))


#Movement

#Player 1 Upward Movement
def Player_1_Up():
    if Player_1.ycor()<200:
        y = Player_1.ycor()
        y+=20
        Player_1.sety(y)
    else:
        Player_1.sety(200)

#Player 1 Downward Movement
def Player_1_Down():
    if Player_1.ycor()>-200:
        y = Player_1.ycor()
        y-=20
        Player_1.sety(y)
    else:
        Player_1.sety(-200)

#Player 2 Upward Movement
def Player_2_Up():
    if Player_2.ycor()<200:
        y = Player_2.ycor()
        y+=20
        Player_2.sety(y)
    else:
        Player_2.sety(200)


#Player 2 Downward Movement
def Player_2_Down():
    if Player_2.ycor()>-200:
        y = Player_2.ycor()
        y-=20
        Player_2.sety(y)
    else:
        Player_2.sety(-200)


#Keyboard Binding
window.listen()
window.onkeypress(Player_1_Up,"w")
window.onkeypress(Player_1_Down,"s")
window.onkeypress(Player_2_Up,"Up")
window.onkeypress(Player_2_Down,"Down")

#Main 
#Continues until a player wins and application is closed
while True:
    window.update()
    newx = Ball.xcor() + Ball.dx
    newy = Ball.ycor() + Ball.dy
    Ball.setx(newx)
    Ball.sety(newy)
    #Border Checking
    #Ball reaches top of the screen
    if Ball.ycor() > 190:
        Ball.sety(190)
        Ball.dy*=-1
    #Ball reaches botton of the screen
    elif Ball.ycor() < -190:
        Ball.sety(-190)
        Ball.dy*=-1
    #If player 1 misses the ball the code is executed 
    if Ball.xcor() > 390:
        #Score and scoreboard is updated
        Player_1_score+=1
        Pen.clear()
        Pen.write("{}: {}  {}: {}".format(Player_1_name,Player_1_score,Player_2_name,Player_2_score),align="center",font=("courier",24,"normal"))
        Ball.goto(0,0)
        Ball.dx*=-1
    #If player 2 misses the ball the code is executed
    elif Ball.xcor() < -390:
        #Score and scoreboard is updated
        Player_2_score+=1
        Pen.clear()
        Pen.write("{}: {}  {}: {}".format(Player_1_name,Player_1_score,Player_2_name,Player_2_score),align="center",font=("courier",24,"normal"))
        Ball.goto(0,0)
        Ball.dx*=-1
    #Ball bounces off of player 1 paddle
    if (-350<Ball.xcor()<-340) and Ball.ycor()<=Player_1.ycor()+50 and Ball.ycor()>=Player_1.ycor()-50:
        Ball.dx*=-1
    #Ball bounces off of player 2 paddle
    if (340<Ball.xcor()<350) and Ball.ycor()<=Player_2.ycor()+50 and Ball.ycor()>=Player_2.ycor()-50:
        Ball.dx*=-1
    #Checks if game has ended and a player has won
    if Player_1_score == max_score or Player_2_score == max_score:
        #If player 1 has won code is executed
        if Player_1_score == max_score:
            Pen.clear()
            Pen.goto(0,0)
            Pen.write("GAME OVER! {} WINS!".format(Player_1_name),align="center",font=("courier",24,"normal"))
            turtle.exitonclick()
        #If player 2 has won code is executed
        else:
            Pen.clear()
            Pen.goto(0,0)
            Pen.write("GAME OVER! {} WINS!".format(Player_2_name),align="center",font=("courier",24,"normal"))
            turtle.exitonclick()
            
