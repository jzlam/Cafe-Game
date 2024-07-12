
from cmu_graphics import *
from PIL import Image
import math
import os, pathlib 

class chair: 
    def __init__(self, X, Y, pic):
        
        self.x = X 
        self.y = Y

        self.rows = 10 
        self.cols = 10 
        self.tileLen = 50
        
        self.chairSize = 80
        #put in coords for botttom of the parallelogam

        self.chairOrder = [[] for i in range(6)]
        self.hasCustomer = False

        self.possiblePositions = [([[0,0]] * self.cols) for row in range(self.rows)]
        self.beginningX = 15
        self.beginningY = 15
        self.findPossiblePositions()

        self.empty = True 

        self.chairPic = Image.open('images/chair.png')
        self.chairPic = self.chairPic.resize((self.chairSize,120))
        self.chairPic = CMUImage(self.chairPic)

        self.chairFullPic = Image.open(f'images/{pic}Chair.png')
        self.chairFullPic = self.chairFullPic.resize((self.chairSize,120))
        self.chairFullPic = CMUImage(self.chairFullPic)

        

        #check if table is full or not 

    def drawChair(self):
        x,y = self.possiblePositions[self.x][self.y]
        if self.empty == True:
            drawImage(self.chairPic, x, y, align = "center")
        elif self.empty == False:
            drawImage(self.chairFullPic, x, y, align = "center")


    def findPossiblePositions(self): 
        for row in range(self.rows): 
            for col in range(self.cols): 
                self.possiblePositions[row][col] = [(self.beginningX+((row) * self.tileLen)), (self.beginningY +(col * self.tileLen))]
                self.possiblePositions[row][col] = self.toIsometric(self.possiblePositions[row][col], 400,200) 
    
    def toIsometric(self, tuple , topX, topY  ) : #tuple = x,y
        XTwoD = tuple[0]*(math.cos(math.radians(210))) + tuple[1]*(math.cos(math.radians(330))) 
        YTwoD = tuple[0]*(math.sin(math.radians(210))) + tuple[1]*(math.sin(math.radians(330))) 
        newX = topX + XTwoD 
        newY = topY - YTwoD
        return [newX, newY]
        