from cmu_graphics import * 
import random
import math 
from PIL import Image
import os, pathlib 

class customer:
    chairNum  = 0
    def __init__(self, color):
        self.menu = ["bread", "lettuce","meat"]
        self.onChair = False
        self.color = color 
        self.tableNum = customer.chairNum % 6
        customer.chairNum += 1  

        self.arriving = True
        self.size = 10

        self.rows = 10 
        self.cols = 10 
        self.tileLen = 50

        self.possiblePositions = [([[0,0]] * self.cols) for row in range(self.rows)]
        self.beginningX = 15
        self.beginningY = 15

        self.findPossiblePositions()

        self.chairSize = 80

        self.posNum = 0
        self.customerPaths = [
            #table 0
            [("n/a",100), (0,0), (1,0), (1,1), (2,1),(3,1), (4,1), (5,1),(6,1),(7,1),(7,2), (7,3)],
            #table 1 
            [("n/a",100),(0,0),(1,0), (1,1), (2,1),(2,2), (2,3), (2,4),(2,5),(3,5),(4,5), (5,5), (6,5), (7,5), (7,6) ],
            #table 2
            [("n/a",100),(0,0),(1,0), (2,0), (2,1),(2,2), (2,3), (2,4),(2,5), (2,6), (2,7),(2,8),(3,8),(4,8), (5,8), (6,8), (7,8), (7,9) ],
            #table 3
            [("n/a",100),(0,0),(1,0), (1,1), (2,1),(3,1), (4,1), (4,2),(4,3)],
            #table 4
            [("n/a",100),(0,0),(1,0), (1,1), (2,1),(3,1), (3,2), (3,3), (3,4),(3,5), (4,5), (4,6)],
            #table 5 
            [("n/a",100),(0,0),(1,0), (1,1), (2,1),(3,1), (3,2),(3,3), (3,4),(3,5), (3,6),(3,7), (3,8),(4,8), (4,9)]
            ]
        self.position = None 

        self.order = self.placeFoodOrder()
    
        self.labelY = 130 + (50* self.tableNum)
        self.showOrder = False 

        self.custPic = Image.open(f'images/{color}Pic.png')
        self.custPic = self.custPic.resize((80,80))
        self.custPic = CMUImage(self.custPic)

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

    def placeFoodOrder(self): 
        order = ["bread"]
        numOfItems = random.randint(1,3)
        for i in range(numOfItems):
            order += [random.choice(self.menu)]
        self.payment = numOfItems * (random.randint(1,3))
        return order

    def drawCustomers(self): 
        if self.onChair == False:    
            self.path = self.customerPaths[self.tableNum]
            gridX, gridY = self.path[self.posNum][0], self.path[self.posNum][1]
            if gridX != "n/a":
                finalx,finaly = self.possiblePositions[gridX][gridY]
                self.position = [finalx, finaly] 
                drawImage(self.custPic, self.position[0] + self.tableNum * 5, self.position[1], align = "center")
            else: 
                drawCircle (10000,1000,4)
        
        if self.showOrder == True: 
            orderStr = "- "
            for ingredient in self.order: 
                orderStr += f'{ingredient}, '
            orderStr = orderStr[0:-2]
            drawLabel(f'{orderStr}', 920, self.labelY, fill = self.color , size = 17, align = "left-top", bold = True)





            
            