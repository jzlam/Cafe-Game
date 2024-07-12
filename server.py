from cmu_graphics import * 
import math
from PIL import Image
#write table class

class server:
    def __init__(self):
        self.topX = 400 #Top of XYZ Plane where z is 0
        self.topY = 200

        self.size = 10 
        self.moveLen = 80

        self.gridPosition = [3,0] #row,col
        self.ThreeDPosition = [15, 15- (self.size/2)] #(x,y,z) but z is 0 , current position , starts in first Grid
        
        self.holding = []  

        self.rows = 10 
        self.cols = 10 
        self.tileLen = 50
        self.possiblePositions = [([[0,0]] * self.cols) for row in range(self.rows)] #center of the tiles in a 2dList
        self.beginningX = 15
        self.beginningY = 15

        self.findPossiblePositions()

        self.serverPic = Image.open('images/server.png')
        self.serverPic = self.serverPic.resize((80,80))
        self.serverPic = CMUImage(self.serverPic)

        self.serverPlatePic = Image.open('images/serverWithPlate.png')
        self.serverPlatePic = self.serverPlatePic.resize((80,80))
        self.serverPlatePic = CMUImage(self.serverPlatePic)


    def findPossiblePositions(self): 
        for row in range(self.rows): 
            for col in range(self.cols): 
                self.possiblePositions[row][col] = [(self.beginningX+((row) * self.tileLen)), (self.beginningY +(col * self.tileLen))]
                self.possiblePositions[row][col] = self.toIsometric(self.possiblePositions[row][col])
    
    def draw(self): 
        self.TwoDPosition = [self.toIsometric(self.ThreeDPosition)[0],self.toIsometric(self.ThreeDPosition)[1]]
        row = self.gridPosition[0]
        col = self.gridPosition[1]
        X,Y = self.possiblePositions[row][col]
        if len(self.holding) == 0: 
            drawImage(self.serverPic, X, Y, align = "center")
        else: 
            drawImage(self.serverPlatePic, X, Y, align = "center")
        

    def toIsometric(self, tuple ) : #tuple =[x,y]
        XTwoD = tuple[0]*(math.cos(math.radians(210))) + tuple[1]*(math.cos(math.radians(330))) 
        YTwoD = tuple[0]*(math.sin(math.radians(210))) + tuple[1]*(math.sin(math.radians(330))) 
        newX = self.topX + XTwoD 
        newY = self.topY - YTwoD
        return [newX, newY] 
    
    def moveUp(self):
        self.ThreeDPosition[0] -= self.moveLen
        self.gridPosition[0] -= 1 
    def moveDown(self):
        self.ThreeDPosition[0] += self.moveLen
        self.gridPosition[0] += 1 
    def moveRight(self):
        self.ThreeDPosition[1] += self.moveLen
        self.gridPosition[1] += 1 
    def moveLeft(self): 
        self.ThreeDPosition[1] -= self.moveLen
        self.gridPosition[1] -= 1 
    def movesItem(self, item): # places or picks up 
        self.holding = [item]


    

