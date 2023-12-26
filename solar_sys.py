import turtle
import math
from math import *

class Planet(turtle.Turtle):
    def __init__(self,name,radius, color):
        super().__init__(shape='circle')#наследование круглой формы
        self.name = name
        
        self.radius = radius
        
        self.c = color
        self.color(self.c)
        
        self.angle = 0
        
    def moving(self):
        x = self.radius*cos(self.angle)
        y = self.radius*sin(self.angle)
        self.goto(sun.xcor()+x,sun.ycor()+y)
        #абсолютная позиция черепахи

sun = turtle.Turtle()
sun.shape('circle')
sun.color('yellow')

venus = Planet("venus",40, 'purple')

mercury = Planet("mercury",20, 'grey')

earth=Planet("earth",60,'blue')

mars = Planet("mars",80, 'red')

jupiter=Planet("jupiter",100, 'orange')

saturn=Planet("saturn",120, 'brown')

uranus=Planet("uranus",140, 'dark blue')

neptune=Planet("neptune",160, 'light blue')

endinga = Planet("eee",180, 'white')
 
planets=[mercury, venus,earth, mars,jupiter,saturn,uranus,neptune, endinga]

sc = turtle.Screen()
sc.tracer(45)
while True:
    sc.update()
    for i in planets:
        i.moving()
   
    venus.angle += 0.02
    
    mercury.angle += 0.03

    earth.angle += 0.04

    mars.angle += 0.02

    jupiter.angle += 0.03

    saturn.angle += 0.015

    uranus.angle += 0.017

    neptune.angle += 0.004
    endinga.angle += 0.006
