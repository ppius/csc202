from turtle import *
import random, math


def snowflakePart(distance, cutoff, depth):
    if depth > cutoff:
        forward(distance)
    else:
        snowflakePart(distance, cutoff, depth+1)
        left(60)
        snowflakePart(distance, cutoff, depth+1)
        right(120)
        snowflakePart(distance, cutoff, depth+1)
        left(60)
        snowflakePart(distance, cutoff, depth+1)


def snowflake(distance, cutoff, x, y):
    color(random.choice(['red','green','blue','black']))

    penup()
    width = distance*3**(cutoff+1)
    widthB = distance*3**(cutoff)
    height = (width-widthB)*math.sin(math.radians(60))
    setpos(x-width/2,y+height/2)
    pendown()
    setheading(0)

    for i in range(0, 3):
        snowflakePart(distance, cutoff, 0)
        right(120)


def clickFunction(x,y):

    if random.randint(0,1) <= 0:
        tracer(False)
        pensize(1)
        snowflake(1,4,x,y)
        update()
    else:
        tracer(True)
        speed(10)
        pensize(2)
        snowflake(3,2,x,y)


def snowPicture():

    resetscreen() 
    pensize(3)
    tracer(False)
    cutoff = 2

    for d in [1, 2, 3, 5, 10, 14, 20]:
        snowflake(d,cutoff,0,0)
    update()

    penup()
    setpos(0,-100)
    pencolor('black')
    write('Click screen for more snowflakes!',
          align='center', font=('Ariel', 18, 'bold'))    

    onscreenclick(clickFunction)

    mainloop()


snowPicture()
