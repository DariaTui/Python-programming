import math
import turtle
roza=turtle.Turtle()
roza.speed(0)
roza.pencolor('red')
b=3
a=300
for i in range(1000):
    r=a*math.sin(b*i)
    x=r*math.cos(i)
    y=r*math.sin(i)
    roza.up()
    roza.goto(x,y)
    roza.down()
    roza.dot()
turtle.exitoniclick()
