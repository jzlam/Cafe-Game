from cmu_graphics import * 
from PIL import Image
import os, pathlib 
import math 

class cafe: 
    def __init__(self, rows, cols):
        
        self.rows = rows
        self.cols = cols
        self.tileLen = 50

        self.topX  = 400 # in relation to the 2D python view 
        self.topY = 200 

        #OutermostEdgePoints) in the 2D Plane(Rectangle
        self.TwoDTopLeftPoint = (0,0)
        self.TwoDTopRightPoint = (0, (self.tileLen * self.rows))
        self.TwoDBottomLeftPoint= ((self.tileLen * self.cols), 0)
        self.TwoDBottomRightPoint = ((self.tileLen * self.cols) , (self.tileLen * self.rows))

        #EdgePoints in the XY plane (parallelogram)
        self.ThreeDTopPoint = self.toIsometric(self.TwoDTopLeftPoint)
        self.ThreeDLeftPoint = self.toIsometric(self.TwoDBottomLeftPoint)
        self.ThreeDRightPoint = self.toIsometric(self.TwoDTopRightPoint)
        self.ThreeDBottomPoint = self.toIsometric(self.TwoDBottomRightPoint )

        self.floor = [([None] * app.cols) for row in range(app.rows)]
        self.tables = []

        self.notesPic = Image.open('images/notes.jpeg')
        #self.notesPic = self.notesPic.resize((self.tableSize,self.tableSize))
        self.notesPic = CMUImage(self.notesPic)

    def placeTables(self, mouseX, mouseY):
        X, Y = self.undoIsometric((mouseX, mouseY))
        print(X,Y)
        row,col = self.getCell(X, Y)

        self.floor[row][col] = "table"

    def getCell(self,X,Y) :
        for row in range(self.rows):
            for col in range(self.cols): 
                if (row * self.tileLen < Y < (row+1) * self.tileLen) and (col * self.tileLen < X < (col+1) * self.tileLen):
                    return row,col

# I learned this from https://docs.google.com/presentation/d/10Ai3ksLtZXHL4JyUL0pGqOiqL8JTEEjiDO_nKXiv9GA/edit#slide=id.gf78fa600fd_0_567 
    def toIsometric(self, tuple ) : #tuple = x,y
        XTwoD = tuple[0]*(math.cos(math.radians(210))) + tuple[1]*(math.cos(math.radians(330))) 
        YTwoD = tuple[0]*(math.sin(math.radians(210))) + tuple[1]*(math.sin(math.radians(330))) 
        newX = self.topX + XTwoD 
        newY = self.topY - YTwoD
        return newX, newY
    

    def undoIsometric(self, tuple):
        X = tuple[0] - self.topX 
        Y = -(tuple[1] - self.topY)
        x = X*(math.cos(math.radians(150))) + Y*(math.cos(math.radians(30)))
        y = X*(math.sin(math.radians(150))) + Y*(math.sin(math.radians(30)))
        return (x,y)
    
    def drawFloor(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.floor[row][col] == None:
                   self.drawTile(row, col)
        drawImage(self.notesPic, 900,100, align = "left-top")
    
    def drawTile(self, row, col):
        beforeLeftTopPoint = (self.getLeftTopPoint(row,col)[0],self.getLeftTopPoint(row,col)[1])
        beforeRightTopPoint = (beforeLeftTopPoint[0],beforeLeftTopPoint[1] + self.tileLen)
        beforeBottomLeftPoint = (self.getBottomLeftPoint(row,col)[0],self.getBottomLeftPoint(row,col)[1])
        beforeBottomRightPoint = (beforeBottomLeftPoint[0],beforeBottomLeftPoint[1] + self.tileLen)

        leftTopPoint = self.toIsometric(beforeLeftTopPoint)
        rightTopPoint = self.toIsometric(beforeRightTopPoint)
        bottomLeftPoint = self.toIsometric(beforeBottomLeftPoint)
        bottomRightPoint = self.toIsometric(beforeBottomRightPoint)

        drawPolygon(rightTopPoint[0], rightTopPoint[1], 
                bottomRightPoint[0], bottomRightPoint[1],
                bottomLeftPoint[0], bottomLeftPoint[1],
                leftTopPoint[0], leftTopPoint[1],
                fill = None, border = 'black', borderWidth = .25)
        
    def getLeftTopPoint(self,row,col): #Gets you the new LeftTopPoint in the XY Plane before transforming
        newX = self.TwoDTopLeftPoint[0] + (self.tileLen*row)
        newY = self.TwoDTopLeftPoint[1] + (self.tileLen*col)
        return (newX, newY)
    
    def getBottomLeftPoint(self,row,col): #Gets you the new bottomLeftPoint in the XY Plane before transforming
        newX = (self.TwoDTopLeftPoint[0]+self.tileLen) + (self.tileLen*row)
        newY = self.TwoDTopLeftPoint[1] + (self.tileLen*col)
        return (newX, newY)


    

        
    

