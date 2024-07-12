from cmu_graphics import *
from PIL import Image
import os, pathlib 

class table: 
    def __init__(self, X, Y):
        self.x = X 
        self.y = Y
        
        self.tableSize = 80
        #put in coords for botttom of the parallelogam

        self.order = []
        self.hasCustomer = False
        self.hasPlate = False

        #check if table is full or not 

    def drawTable(self):
            if self.hasPlate == False: 
                tablePic = Image.open('images/table.png')
                tablePic = tablePic.resize((self.tableSize,self.tableSize))
                tablePic = CMUImage(tablePic)
                drawImage(tablePic, self.x, self.y, align = "center")
            if self.hasPlate == True: 
                tablePic = Image.open('images/tableFull.png')
                tablePic = tablePic.resize((self.tableSize,self.tableSize))
                tablePic = CMUImage(tablePic)
                drawImage(tablePic, self.x, self.y, align = "center")

                


