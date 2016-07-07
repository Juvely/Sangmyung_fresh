import turtle, random
wn = turtle.Screen()
b1 = turtle.Turtle()
go = turtle.Turtle()


#<<나의 터틀>>
miso = turtle.Turtle()
#<<적터틀>>
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
king = turtle.Turtle()
#<<3번째 아이템을 먹을 때 나오는 나의 총>>
gun = turtle.Turtle()
#<<랜덤 아이템>>
itemtt = turtle.Turtle()

        
def Screen():
    wn.setup(700, 700)
      
    b1.pencolor("Green") 
    b1.penup()
    b1.goto(-300, -300) 
    b1.pendown()

    for i in range(4): 
        b1.ht()
        b1.fd (600)
        b1.lt (90)

#<<기본 설정>>
def seting():
    miso.color("pink")
    miso.shape("turtle")
    t1.shape('turtle'), t2.shape('turtle'), t3.shape('turtle'), t4.shape('turtle'), king.shape('turtle')
    king.color("green")
    t1.pu()
    gun.pencolor("red")
    gun.ht()
    itemtt.shape("square")
    itemtt.color("pink")
    go.ht()

    t1.shapesize(2,2,0)
    t2.shapesize(4,4,0)
    t3.shapesize(6,6,0)
    t4.shapesize(8,8,0)



#<<miso 움직이기>>
    
def setEvent():
    wn.onkey(keyUp,"Up")
    wn.onkey(keyRight,"Right")
    wn.onkey(keyLeft,"Left")
    wn.onkey(Gun,"space")

    wn.listen()


def keyUp():
    miso.fd(15)


def keyRight():
    miso.right(random.randint(10,20))


def keyLeft():
    miso.left(random.randint(10,20))


#<<게임에 필요한 함수들>>
def act(t,num):
    
    t.seth(t.heading()+random.randint(-90,90))
    t.fd(8)

    if (miso.distance(t) <= num ):
        miso.color('red')
        
        gameOver()

def line(k):
    
    if k.pos()[0]< -290:
        k.goto( -200  ,k.pos()[1])
    if k.pos()[0]>290:
        k.goto( 200  ,k.pos()[1])

    if k.pos()[1] <-290:
        k.goto(k.pos()[0], -200)
    if k.pos()[1] >290:
        k.goto(k.pos()[0], 200)

def rando(a):
    a.pu()
    a.goto(random.randint(-230, 230), random.randint(-230, 230))

#<<game Over & game Clear>>

def gameOver():
    go.ht()
    go.pencolor("Red")
    p = wn.textinput("Game_Over","What's your name : ")
    go.write(p +"... You Die..", align = "center", font = ("",20,"bold"))

def gameOver2():
    go.ht()
    go.pencolor("Red")
    p = wn.textinput("Game_Over","What's your name : ")
    go.write("king killed "+p, align = "center", font = ("",20,"bold"))
    
def win():
    go.ht()
    go.pencolor("Red")
    p = wn.textinput("Congratulation","What's your name : ")
    go.write(p + " ! You are Winner! King is Die! ", align = "center", font = ("",20,"bold"))
    

#<<마구잡이로 움직이는 터틀과 게임 핵심 부분>>
def item_n_GradeC(): 
       
    t2.ht()
    t3.ht()
    t4.ht()
    king.ht()
    gun.ht()

    t1.goto(random.randint(-230, 230), random.randint(-230, 230))
    rando(t2)
    rando(t3)
    rando(t4)
    rando(king)
    
    score = 0
    speed = 0
    count = 0

    itemtt.pu()

    #<<아이템>>
    while True:


        if miso.xcor() < -300 or miso.xcor() > 300:
            gameOver()
            miso.ht()

        elif miso.ycor() < -300 or miso.ycor() > 300:
            gameOver()
            miso.ht()
            
        #random으로 움직이는 t1
        t1.seth(t1.heading()+random.randint(-90,90))
        t1.fd(10)

        #item        
        r1 = itemtt.xcor() + 15
        r2 = itemtt.xcor() - 15
        r3 = itemtt.ycor() + 15
        r4 = itemtt.ycor() - 15

        if (miso.xcor() >= r2 and miso.xcor() <= r1) and (miso.ycor() >= r4 and miso.ycor() <= r3):
            itemtt.goto(random.randint(-290, 290), random.randint(-290, 290))
            score += 1
            speed += 1
            count += 1

            if (count == 5):
                itemtt.color("white")
    
        if (miso.distance(t1) <= 15 ):
            miso.color('red')
            
            gameOver()
            
         #아이템 먹으면 등장하는 신하터틀
            
        if (count >= 2) :
            t2.st()
            act(t2,32)

        if (count >= 3) :
            t3.st()
            act(t3,45)

        if (count >= 4) :
            t4.st()
            act(t4,63)

        if (count >= 5) :
            king.st()
            gun.st()            
            king.seth(king.heading()+random.randint(-90,90))
            king.fd(10)

            if (miso.distance(king) <= 10 ):
                miso.color('red')
        
                gameOver2()


        if king.pencolor() == "red":
            king.write("Die")
            win()

        #적 터틀 관련

        line(t1)
        line(t2)
        line(t3)
        line(t4)
        line(king)

#<<왕을 죽일 총>>
        
def Gun(): 
    gun.ht()
    gun.pu()
    gun.goto(miso.pos())
    gun.seth(miso.heading())
    gun.st()
    gun.pd()
    gun.speed(10)

    for i in range(0,20):
        gun.fd(13)
        
        if (gun.distance(king) < 15 ):
            king.color("red")

def start():
    Screen()
    seting()
    setEvent()
    item_n_GradeC()

    
    
start()
