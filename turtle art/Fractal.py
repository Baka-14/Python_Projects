from turtle import *
import random

speed(0) #to draw fast when required 

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
    

create_snowflake(3,200)
hideturtle()
mainloop()


