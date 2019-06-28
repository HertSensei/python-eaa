import time
import turtle
import random

#screen setup
screen = turtle.Screen()
screen.title('snake game hehe')
screen.setup(width = 600 , height = 700)
screen.bgcolor('blue')
screen.tracer(0)

delay = 0.2

# pen
score = turtle.Turtle()

score.penup()
score.speed(0) 
score.shape('square')
score.hideturtle()
score.write('score :0' ,align='center' , font=("Courier",0,"normal"))
score.color('white')
score.goto(2,280)



#head
head =turtle.Turtle()
head.color('black')
head.speed(0)
head.shape('square')
head.penup()

head.goto(0,0)
head.direction = 'stop'

# the food 
food =turtle.Turtle()
food.color('yellow')
food.speed(0)
food.shape('circle')
food.penup()
food.goto(0,100)

# define segments
segments = []
# jika score lebih tinggi dari 100
obs = turtle.Turtle()
obs.speed(0)
obs.shape('square')
def halangan():
    
    obs.penup()
    obs.color('red')
    obs.goto(0,200)
    obs.direction = 'right'

obs2 = turtle.Turtle()
obs2.speed(0)
obs2.shape('square')
    
def halangan2():
    
    obs2.penup()
    obs2.color('red')
    obs2.goto(20,-230)
    obs2.direction = 'right'


obs3 = turtle.Turtle()
obs3.speed(0)
obs3.shape('square')

def halangan3():
    
    obs3.penup()
    obs3.color('red')
    obs3.goto(100,200)
    obs3.direction = 'right'

obs4 = turtle.Turtle()
obs4.speed(0)
obs4.shape('square')

def halangan4():
    
    obs4.penup()
    obs4.color('red')
    obs4.goto(-30,-60)
    obs4.direction = 'right'



    if obs.direction == 'right' :
        x = obs.xcor()
        obs.setx( x + 20)


    if obs.xcor() > 290 :
        x = obs.xcor()
        obs.direction = 'left'
        obs.setx(x - 20)


#movement function

def headUp() :
    if head.direction != 'down':
        head.direction = 'up'

def headRight() :
    if head.direction != 'left':
        head.direction = 'right'


def headLeft() :
    if head.direction != 'right':
        head.direction = 'left'


def headDown() :
    if head.direction != 'up':
        head.direction = 'down'

def headStop() :
    head.direction = 'stop'

def move ():
    if head.direction == "up" :
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "right" :
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left" :
        x = head.xcor()
        head.setx(x - 20)


    if head.direction == "down" :
        y = head.ycor()
        head.sety(y - 20)

#listen the key press
screen.listen()
screen.onkeypress(headUp, 'w')
screen.onkeypress(headDown, 's')
screen.onkeypress(headLeft, 'a')
screen.onkeypress(headRight, 'd')
screen.onkeypress(headStop, 'v')

# skor
skor = 0
high_score = 0
#membuat layar tetap terlihat
#screen update
while True :
    screen.update()
    # if head collision the food , food will go to random places on screen
    if head.distance(food) < 20 :
        x = random.randint(-140,170)
        y = random.randint(-160,200)
        food.goto(x,y)
        skor+=20
        
        if skor >= 100:
            halangan()
        if skor >= 160:
            halangan2()
        if skor >=180:
            halangan3()
        if skor >= 220:
            halangan4()


    # body will append when head touch the food
        body = turtle.Turtle()
        body.color('grey')
        body.penup()
        body.shape('square')
        body.speed(0)
        segments.append(body)

        if skor > high_score:
            high_score = skor
        score.clear()


        score.write("Score = {} High Score = {}".format(skor,high_score),align='center',font=("Courier",24,'normal'))

        

    # jika body menabrak batas screen
    if head.xcor()> 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        head.direction = 'stop'
        head.goto(0,0) 
        time.sleep(1)
        
        
    
        
        for segment in segments:
            segment.goto(9000,9000)
            segments.clear()
        skor = 0
        score.clear()
        score.write("Score = {} High Score = {}".format(skor,high_score),align='center',font=("Courier",24,'normal'))


    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

        
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # cek apakah menabrak body
    for segment in segments:
        if segment.distance(head) < 20 or segment.distance(obs) < 20 or segment.distance(obs2) < 20 or segment.distance(obs3) < 20 or segment.distance(obs4) < 20:
            time.sleep(1.5)
            head.goto(0,0)
            head.direction ="stop"

            # hide segments
            for segment in segments:
                segment.goto(2000,1000)


            # clear segment
            segments.clear()
            
            skor = 0
            score.clear()
            score.write("Score = {} High Score = {}".format(skor,high_score),align='center',font=("Courier",24,'normal'))


    time.sleep(delay)

screen.mainloop()