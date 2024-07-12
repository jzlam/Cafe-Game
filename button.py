from cmu_graphics import *
from PIL import Image
import os, pathlib 

class button: 
    def __init__(self,x,y,fun):    
        self.x = x
        self.y = y
        self.size = 10
        self.fun = fun

    def draw(self):
        drawCircle(self.x,self.y, self.size , fill = "red" )

    def checkForPress(self, app, mX, mY):
        if ((mX - self.x)**2 + (mY-self.y)**2)**0.5 <= self.size:
            self.fun(app)

class rectangleButton: #only tutorial button
    def __init__(self,x,y, w, h, fun):
        self.x =x
        self.y = y 
        self.width = w 
        self.height = h
        self.fun = fun 

    def draw(self):
        drawRect(self.x, self.y, self.width, self.height, border = "black", fill = "white" , borderWidth = 2)
        drawLabel( "Tutorial", self.x + (self.width * .5), self.height , size = 20) 

    def checkForPress(self, app, mX, mY):
        if (self.x < mX < (self.x + self.width)) and (self.y < mY < (self.y + self.height)) :
            self.fun(app)             






