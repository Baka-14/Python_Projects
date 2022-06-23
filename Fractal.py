from turtle import *
import random
import turtle

speed(0) #to draw fast when required 

turtle.screensize(canvwidth=500,canvheight=500,bg="light blue")
def snowflake_side(length,levels):
    if levels==0:
        forward(length)
        return
    length/=3.0
    snowflake_side(length,levels-1)
    left(60)
    snowflake_side(length,levels-1)
    right(120)
    snowflake_side(length,levels-1)
    left(60)
    snowflake_side(length,levels-1)


def create_snowflake(sides,length):
    for _ in range(sides):
        snowflake_side(length,sides)
        right(360/sides)
    
for _ in range(5):
    x=random.randint(2,5)
    y=random.randint(100,400)
    turtle.up()
    pos=[random.randint(10,300),random.randint(10,300)]
    goto(pos[0],pos[1])
    left(90)
    turtle.down()
    create_snowflake(x,y)

hideturtle()
mainloop()


