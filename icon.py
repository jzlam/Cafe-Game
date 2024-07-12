from cmu_graphics import *
from PIL import Image

class icon: 
    def __init__(self, type,x,y):
        self.icons = [] 
        self.type = type 
        self.x = x
        self.y = y
        self.size = 80
        
        self.stoveFull = False
        self.stoveEmptyPic = Image.open('images/stoveEmpty.png')
        self.stoveEmptyPic = self.stoveEmptyPic.resize((self.size,self.size))
        self.stoveEmptyPic = CMUImage(self.stoveEmptyPic)

        self.stoveFullPic = Image.open('images/stoveFull.png')
        self.stoveFullPic = self.stoveFullPic.resize((self.size,self.size))
        self.stoveFullPic = CMUImage(self.stoveFullPic)

        self.stoveProgress = 1 
        self.cooking = False

        self.cutting = False 
        self.cuttingEmptyPic = Image.open('images/cuttingEmpty.png')
        self.cuttingEmptyPic = self.cuttingEmptyPic.resize((self.size,self.size))
        self.cuttingEmptyPic = CMUImage(self.cuttingEmptyPic)

        self.cuttingFullPic = Image.open('images/cuttingFull.png')
        self.cuttingFullPic = self.cuttingFullPic.resize((self.size,self.size))
        self.cuttingFullPic = CMUImage(self.cuttingFullPic)

        self.cuttingProgress = 1

        self.garbagePic = Image.open('images/garbage.png')
        self.garbagePic = self.garbagePic.resize((self.size,self.size))
        self.garbagePic = CMUImage(self.garbagePic)
            

    def draw(self):
        if self.type == "lettuce": 
            lettucePic = Image.open('images/lettuceBin.png')
            lettucePic = lettucePic.resize((self.size,self.size))
            lettucePic = CMUImage(lettucePic)
            drawImage(lettucePic, self.x,self.y, align = "center")
        elif self.type == "bread": 
            breadPic = Image.open('images/breadBin.png')
            breadPic = breadPic.resize((self.size,self.size))
            breadPic = CMUImage(breadPic)
            drawImage(breadPic, self.x,self.y, align = "center")
        elif self.type == "burger": 
            burgerPic = Image.open('images/burgerBin.png')
            burgerPic = burgerPic.resize((self.size,self.size))
            burgerPic = CMUImage(burgerPic)
            drawImage(burgerPic, self.x,self.y, align = "center") 
        elif self.type == "stoveEmpty": 
            drawImage(self.stoveEmptyPic, self.x,self.y, align = "center")
            
        elif self.type == "stoveFull": 
            drawImage(self.stoveFullPic, self.x,self.y, align = "center")
            drawRect(673,335, 60, 10, fill = "white", border = "black", borderWidth = 2 )
            drawRect(675,337, self.stoveProgress, 6 , fill = "green" )

        elif self.type == "cutting":
            if self.cutting == False:
                drawImage(self.cuttingEmptyPic, self.x,self.y, align = "center")     
            elif self.cutting == True:
                drawImage(self.cuttingFullPic, self.x,self.y, align = "center")
                drawRect(713,360, 60, 10, fill = "white", border = "black", borderWidth = 2 )
                drawRect(715,362, self.cuttingProgress , 6, fill = "green" )

        elif self.type == "garbage": 
            drawImage(self.garbagePic, self.x,self.y, align = "center")

        self.icons += [[self.x,self.y]]

