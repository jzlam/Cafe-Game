from cmu_graphics import *
from PIL import Image
import os, pathlib 

class counter: 
    def __init__(self, X, Y ):
        self.x = X 
        self.y = Y
        self.position = (0,9)
        self.ingredients = [] 

        self.size = 80 
        self.emptyPic = Image.open("images/counter.png" )
        self.emptyPic = self.emptyPic.resize((self.size,self.size))
        self.emptyPic = CMUImage(self.emptyPic)
        
        self.ingredientY = Y

        self.breadPic = Image.open("images/bread.png" )
        self.breadPic = self.breadPic.resize((self.size,self.size))
        self.breadPic = CMUImage(self.breadPic)

        self.lettucePic = Image.open("images/lettuce.png" )
        self.lettucePic = self.lettucePic.resize((self.size,self.size))
        self.lettucePic = CMUImage(self.lettucePic)

        self.meatPic = Image.open("images/meat.png" )
        self.meatPic = self.meatPic.resize((self.size,self.size))
        self.meatPic = CMUImage(self.meatPic)
        

    def drawCounter(self): #draws counter and added ingredients 
        drawImage(self.emptyPic, self.x ,self.y , align = "center")
        
        for ingredientNum in range(len(self.ingredients)): 
            self.ingredientY = self.y - (ingredientNum * 5) 
            if self.ingredients[ingredientNum] == "bread": 
                drawImage(self.breadPic, self.x, self.ingredientY, align = "center" )
            if self.ingredients[ingredientNum] == "meat":
                drawImage(self.meatPic, self.x, self.ingredientY, align = "center" )
            if self.ingredients[ingredientNum] == "lettuce": 
                drawImage(self.lettucePic, self.x, self.ingredientY, align = "center" )
