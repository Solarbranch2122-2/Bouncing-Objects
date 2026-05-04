from turtle import *
import random
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
def move_heading(t):
    t.forward(5)
    if t.xcor()>340 or t.xcor() < -340:
        t.setheading(180-t.heading())
        t.forward(10)
    if t.ycor()>340 or t.ycor() < -340:
        t.setheading(-t.heading())
        t.forward(10)

def move_xy(turtle, deltax, deltay):
    newx = turtle.xcor()+deltax
    newy = turtle.ycor()+deltay
    if newx>340 or newx<-340:
        newx=turtle.xcor()
        deltax*=-1
    if newy>340 or newy<-340:
        newy=turtle.ycor()
        deltay*=-1
    turtle.goto(newx,newy)
    return deltax,deltay
win = Screen()
win.bgcolor("grey")
win.setup(width=750, height=750)

# turtles = []
# for i in range(10):
#     t = Turtle()
#     t.speed(0)
#     t.turtlesize(3,3,3)
#     t.color("white")
#     t.pencolor('black')
#     t.setheading(random.randint(0,360))
#     turtles.append(t)

tur = Turtle()
tur.color("white")
tur.pencolor("white")
tur.speed(0)
tur.shape("circle")
deltax = random.randint(-2,2)
deltay = random.randint(-2,2)

alive = True
while alive == True:
    deltax,deltay=move_xy(tur,deltax,deltay)

    

# screen.onkey(move_up, "Up")
# screen.listen()

win.exitonclick()