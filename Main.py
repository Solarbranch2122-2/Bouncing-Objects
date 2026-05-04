from turtle import *
import random

def move_xy(turtle, deltax, deltay):
    newx = turtle.xcor()+deltax
    newy = turtle.ycor()+deltay
    if newx>340 or newx<-340:
        newx=turtle.xcor()
        deltax*=-1
        create_wall(tur)
    if newy>340 or newy<-340:
        newy=turtle.ycor()
        deltay*=-1
        create_wall(tur)
    turtle.goto(newx,newy)
    return deltax,deltay


def bg():

    background = Turtle()
    background.begin_fill()
    background.speed(0)
    background.hideturtle()
    background.color("black")
    background.pu()
    background.setpos(-340,-340)
    background.pd()
    background.forward(680)
    background.left(90)
    background.forward(680)
    background.left(90)
    background.forward(680)
    background.left(90)
    background.forward(680)
    background.left(90)
    background.end_fill()
bg()

def create_player():
    global player
    player = Turtle()
    player.color("white")
    player.pencolor("white")
    player.speed(0)
    player.shape("circle")

def create_wall(h):
    
    h = Turtle()
    h.color("white")
    h.pencolor("white")
    h.speed(0)
    h.shape("circle")

def up():
    global player
    player.seth(90)
    player.sety(player.ycor()+10)
def down():
    global player
    player.seth(-90)
    player.sety(player.ycor()-10)


def right():
    global player
    player.seth(0)
    player.setx(player.xcor()+10)

def left():
    global player
    player.seth(180)
    player.setx(player.xcor()-10)

win = Screen()
win.bgcolor("#676767")  #haha 67
win.setup(width=750, height=750)
win.listen()
win.onkeypress(create_player,"space")
win.onkeypress(up, "w")
win.onkeypress(down, "s")
win.onkeypress(left, "a")
win.onkeypress(right, "d")


tur = Turtle()
tur.color("white")
tur.pencolor("white")
tur.speed(0)
tur.shape("circle")
deltax = (random.random()-.5)*20
deltay = (random.random()-.5)*20

player = None
turtles = [tur]

alive = True
while alive == True:
    deltax,deltay=move_xy(tur,deltax,deltay)
    
    for i in turtles:
        pass