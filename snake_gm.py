# line 106 is the place where you have to change the code
# that is where the player wins


import turtle
import time
import random

delay = 0.1
score = 0


time_limit=20
start_time=time.time()


wn= turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("Black")
wn.setup(width=600, height=600)
wn.tracer(0)





rules=turtle.Turtle()
rules.speed(0)
rules.shape("square")
rules.color("yellow")
rules.pendown()
rules.hideturtle()
rules.goto(0,0)
time.sleep(1)
rules.write("Snake Game \n Controls: \n Press (W) to move up \n Press (D) to turn right \n Press (A) to turn left \n Press (S) to move down \n You have to collect 5 fruits to win \n and you have 2 minutes to play \n if the timer runs out \n you LOSE", align='center', font=("arial",20,"bold"))
time.sleep(4)
rules.undo()


head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0,0)
head.direction = 'Stop'

food= turtle.Turtle()
colors= random.choice(['red','blue','green','pink','yellow'])
shapes = random.choice(['square','circle','triangle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score:0  ", align="center", font=("arial",24,"bold"))

segments=[]

def goup():
    if head.direction !="down":
        head.direction ="up"
def godown():
    if head.direction !="up":
        head.direction ="down"
def goleft():
    if head.direction !="right":
        head.direction ="left"
def goright():
    if head.direction !="left":
        head.direction ="right"

def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction =="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction =="right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction =="left":
        x=head.xcor()
        head.setx(x-20)

wn.listen()
wn.onkeypress(goup,'w')
wn.onkeypress(godown,'s')
wn.onkeypress(goleft,'a')
wn.onkeypress(goright,'d')

while True:
    wn.update()
    elapsed_time=time.time()-start_time
    count_down=time_limit - int(elapsed_time)

    if elapsed_time>time_limit:

        turtle.color('pink')
        turtle.write('Time is UP' ,align = "center", font=('arial',24,'bold'))
        wn.clear()


    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="Stop"
        colors= random.choice(['red','blue','green','yellow','pink'])
        shapes = random.choice(['square','circle','triangle'])
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score=0
        delay=0.1
        pen.clear()
        pen.write("Score : {} ". format(score),align="center", font=("arial",24,"bold"))
    if head.distance(food)<20:
        x=random.randint(-270,270)
        y=random.randint(-270,270)
        food.goto(x,y)

        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score +=10

        if score==50:
            head.direction="stop"
            wn.clear()
            turtle.write("you have won", font=("Arial", 50, "bold"), align='center')


        pen.clear()
        pen.write("Score:{}".format(score),align="center", font=("arial",24,"bold"))


    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x=head.xcor()
        y= head.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            colors= random.choice(['red','blue','green'])
            shapes = random.choice(['square','circle'])
            for segemnt in segments:
                segment.goto(1000,1000)
            segment.clear()

            score = 0
            delay =0.1
            pen.clear()
            pen.write("Score : {} ". format(score),align="center", font=("arial",24,"bold"))

    time.sleep(delay)


wn.mainloop()
