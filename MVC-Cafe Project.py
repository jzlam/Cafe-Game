from cmu_graphics import *
from cafe import *
from tables import *
from menu import *
from server import *
from icon import *
from button import *
from Chef import * 
from chair import *
from customer import customer as cus
from counter import *
from PIL import Image
import os, pathlib 


def onAppStart(app):
    app.introScreenOn = True 
    app.introScreen = Image.open('images/introScreen.png')
    app.introScreen = CMUImage(app.introScreen)
    app.gamePaused = True 
    app.showTutorial = True
    app.tutorialPic = Image.open('images/tutorial.png')
    app.tutorialPic = CMUImage(app.tutorialPic)
    app.cafeFramePic = Image.open('images/cafeFrame.png')
    app.cafeFramePic = CMUImage(app.cafeFramePic)

    app.stepsPerSecond = 1
    app.rows = 10 
    app.cols = 10 
    
    app.server = server()
    app.chef = chef()
    app.menu = Menu([0], [0], [], [0])
    app.cafe = cafe(app.rows,app.cols)

    app.tableSize = 80
    app.tableCoords = [(183,525 - app.tableSize//2), (313,600 - app.tableSize//2), (443,675 - app.tableSize//2),
                            (313,450 - app.tableSize//2), (443,525 - app.tableSize//2), (573,600 - app.tableSize//2)] 
    app.tables = []
    for tuple in app.tableCoords: 
        x = tuple[0]
        y = tuple[1]
        app.tables+= [table(x,y)]
    
    app.chair0 = chair(7,3, "coral")
    app.chair1 = chair(7,6, "darkOliveGreen")
    app.chair2 = chair(7,9, "cadetBlue")
    app.chair3 = chair(4,3, "steelBlue")
    app.chair4 = chair(4,6, "deepPink")
    app.chair5 =  chair(4,9, "mediumOrchid")
    app.chairs  = [app.chair0,app.chair1 ,app.chair2 ,app.chair3 ,app.chair4 ,app.chair5]
    
    app.objectSize = 80
    #Only One counter for prepared food

    app.counter = counter(790,475 - (app.objectSize//2))

    #HardCoded Items
    app.tableList = [(8,3), (8,6), (8,9), (5,3), (5,6), (5,9)]
    app.chairList   = [(7,3), (7,6), (7,9), (4,3), (4,6), (4,9)]

    app.icons = [[0,3],[0,4], [0,5], [0,6], [0,7], [0,8], [0,9] ]

    app.cus0 = cus("coral")
    app.cus1 = cus("darkOliveGreen")
    app.cus2 = cus("cadetBlue")
    app.cus3 = cus("steelBlue")
    app.cus4 = cus("deepPink")
    app.cus5 = cus("mediumOrchid")
    app.customers = [app.cus0,app.cus1 ,app.cus2,app.cus3, app.cus4,app.cus5]

    app.tutorialButton = rectangleButton(680, 25, 100, 50, showTutorial)
    #CookingButtons
    app.lettuceButton = button(552,321, addLettuce)
    app.breadButton = button(596,346, addBread)
    app.meatButton = button(640,372, addMeat)
    app.cutButton = button(724,420,  cutLettuce)
    app.allButtons = [[app.lettuceButton.x, app.lettuceButton.y], [app.breadButton.x, app.breadButton.y]]

    app.floor = addAlltoFloor(app)


    app.lettuceBin = icon("lettuce",573,350 - (app.objectSize //2) ) #hardcode where to place the button
    app.breadBin = icon("bread", 617, 375 - (app.objectSize //2))
    app.burgerBin= icon("burger", 660, 400 - (app.objectSize //2) )
    app.garbageCan = icon("garbage",530,325 - (app.objectSize //2) )

    
    app.stove = icon("stoveEmpty", 703, 425 - (app.objectSize //2) )
    app.cutting = icon("cutting", 746, 450 - (app.objectSize //2)  )  

    app.score = 0 

    app.largeBreadPic = Image.open("images/bread.png" )
    app.largeBreadPic = app.largeBreadPic.resize((200,200))
    app.largeBreadPic = CMUImage(app.largeBreadPic)

    app.largeMeatPic = Image.open("images/meat.png" )
    app.largeMeatPic = app.largeMeatPic.resize((200,200))
    app.largeMeatPic = CMUImage(app.largeMeatPic)

    app.largeLettucePic = Image.open("images/lettuce.png" )
    app.largeLettucePic = app.largeLettucePic.resize((200,200))
    app.largeLettucePic = CMUImage(app.largeLettucePic)

def showTutorial(app):
    app.showTutorial = True
    if app.showTutorial == True: 
        app.gamePaused = True 

def addAlltoFloor(app): #adds server and objects to floorgrid
    floor = app.cafe.floor    
    [x,y] = app.server.gridPosition
    for row in range(app.rows): 
        for col in range(app.cols): 
            if row == x and col == y: 
                floor[row][col] = "server"
    for tab in app.tableList: 
        (x,y) = tab
        for row in range(app.rows): 
            for col in range(app.cols): 
                if row == x and col == y: 
                    floor[row][col] = "table"
    for object in app.icons: 
        [x,y] = object
        for row in range(app.rows): 
            for col in range(app.cols): 
                if row == x and col == y: 
                    floor[row][col] = "object"
    (x,y) = app.counter.position
    for row in range(app.rows): 
        for col in range(app.cols): 
            if row == x and col == y: 
                floor[row][col] = "counter"

    for chair in app.chairList: 
        (x,y) = chair
        for row in range(app.rows): 
            for col in range(app.cols): 
                if row == x and col == y: 
                    floor[row][col] = "chair"
    return app.cafe.floor

def redrawAll(app):
    app.cafe.drawFloor()
    drawImage(app.cafeFramePic, 0, 0 , align = "left-top")
    drawIcons(app)
    
    app.server.draw() 
    for cust in app.customers: 
        cust.drawCustomers()
    drawButtons(app)
    for chair in app.chairs: 
        chair.drawChair() 
    for table in app.tables: 
        table.drawTable()
    app.counter.drawCounter()
    drawLabel(f'Money Earned: ${app.score}', 60,39, size = 30, align = "left-top" )
    

    drawLabel(f'Current Plate:', 950 , 550, size = 25) 
    
    for ingredientNum in range(len(app.server.holding)): 
            ingredientY = 800 - (ingredientNum * 15) 
            if app.server.holding[ingredientNum] == "bread": 
                drawImage(app.largeBreadPic, 950, ingredientY, align = "center" )
            if app.server.holding[ingredientNum] == "meat":
                drawImage(app.largeMeatPic, 950, ingredientY, align = "center" )
            if app.server.holding[ingredientNum] == "lettuce": 
                drawImage(app.largeLettucePic, 950, ingredientY, align = "center" )
    
    if app.showTutorial == True: 
        drawImage(app.tutorialPic, app.width//2, app.height //2, align = "center")

    if app.introScreenOn:
        drawImage(app.introScreen, 0, 0, align = "left-top")
              
def drawIcons(app):
    app.garbageCan.draw()
    app.lettuceBin.draw()
    app.breadBin.draw()
    app.burgerBin.draw()
    app.stove.draw()
    app.cutting.draw()
def drawButtons(app):
    app.tutorialButton.draw()
    app.lettuceButton.draw()
    app.breadButton.draw()
    app.meatButton.draw()
    app.cutButton.draw()
    
def onKeyPress(app,keys):
    if "space" == keys: 
        app.introScreenOn = False 
    if "escape" == keys: 
            app.showTutorial = False
            app.gamePaused = False
    if not app.gamePaused:    
        if "w" in keys: 
            app.floor[app.server.gridPosition[0]][app.server.gridPosition[1]] = None #removes previous server
            if isLegal(app, "up"):
                app.server.moveUp()
            app.floor[app.server.gridPosition[0]][app.server.gridPosition[1]] = "server" #places current server
        elif "a" in keys: 
            app.floor[app.server.gridPosition[0]][app.server.gridPosition[1]] = None
            if isLegal(app, "left"):
                app.server.moveLeft() 
            app.floor[app.server.gridPosition[0]][app.server.gridPosition[1]] = "server"
        elif "s" in keys:   
            app.floor[app.server.gridPosition[0]][app.server.gridPosition[1]] = None 
            if  isLegal(app, "down"):
                app.server.moveDown() 
            app.floor[app.server.gridPosition[0]][app.server.gridPosition[1]] = "server"
        elif "d" in keys:  
            app.floor[app.server.gridPosition[0]][app.server.gridPosition[1]] = None
            if isLegal(app, "right"):
                app.server.moveRight()
            app.floor[app.server.gridPosition[0]][app.server.gridPosition[1]] = "server"
        elif "b" in keys: 
            if app.server.gridPosition == [1,9]:  #server ready to pick up ingredients 
                if app.server.holding == []:       #server not currently holding items 
                    app.server.holding = app.counter.ingredients    #server picks up counter items
                    app.counter.ingredients = []            #counter is emptied 
            if app.server.gridPosition == [1,3]: #server in front of garbage can 
                app.server.holding = [] 
            # table 0 
            if app.server.gridPosition in [[7,2],[7,4]]:     # table 0 , checks if server is in the correct position to take order
                    if app.tables[0].hasCustomer == True: #checks if customer is at table 
                        takeOrder(app.cus0)
            if app.server.gridPosition in [[8,2],[8,4], [9,3]]: #table 0 checks for server next to table to place order   
                if  len(app.server.holding) > 0: 
                        if app.tables[0].order == app.server.holding: #server holding correct Item and presses b
                            app.tables[0].hasPlate = True 
                            app.server.holding = []
                            app.cus0.showOrder = False
                            
                            #customer leaves 
                            app.chair0.empty = True
                            app.cus0.onChair = False 
                            app.tables[0].hasPlate = False
                            app.cus0.arriving = False 
                            app.score += app.cus0.payment
            
            # table 1 
            if app.server.gridPosition in [[7,5],[7,7]]:     # table 1 , checks if server is in the correct position to take order
                    if app.tables[1].hasCustomer == True: #checks if customer is at table 
                        takeOrder(app.cus1)
            if app.server.gridPosition in [[8,5],[8,7], [9,6]]: #table 1 checks for server next to table to place order   
                if  len(app.server.holding) > 0: 
                        if app.tables[1].order == app.server.holding: #server holding correct Item and presses b
                            app.tables[1].hasPlate = True 
                            app.server.holding = []
                            app.cus1.showOrder = False
                            
                            #customer leaves 
                            app.chair1.empty= True
                            app.cus1.onChair = False 
                            app.tables[1].hasPlate = False
                            app.cus1.arriving = False 
                            app.score += app.cus1.payment
            #table 2 
            if app.server.gridPosition in [[7,8]]:     # table 0 , checks if server is in the correct position to take order
                    if app.tables[2].hasCustomer == True: #checks if customer is at table 
                        takeOrder(app.cus2)
            if app.server.gridPosition in [[8,8],[9,8]]: #table 0 checks for server next to table to place order   
                if  len(app.server.holding) > 0: 
                        if app.tables[2].order == app.server.holding: #server holding correct Item and presses b
                            app.tables[2].hasPlate = True 
                            app.server.holding = []
                            app.cus2.showOrder = False
                            
                            #customer leaves 
                            app.chair2.empty = True
                            app.cus2.onChair = False 
                            app.tables[2].hasPlate = False
                            app.cus2.arriving = False 
                            app.score += app.cus2.payment
            #table 3
            if app.server.gridPosition in [[4,2],[4,4]]:     # table 0 , checks if server is in the correct position to take order
                    if app.tables[3].hasCustomer == True: #checks if customer is at table 
                        takeOrder(app.cus3)
            if app.server.gridPosition in [[5,2],[5,4], [6,3]]: #table 0 checks for server next to table to place order   
                if  len(app.server.holding) > 0: 
                        if app.tables[3].order == app.server.holding: #server holding correct Item and presses b
                            app.tables[3].hasPlate = True 
                            app.server.holding = []
                            app.cus3.showOrder = False
                            
                            #customer leaves 
                            app.chair3.empty = True
                            app.cus3.onChair = False 
                            app.tables[3].hasPlate = False
                            app.cus3.arriving = False 
                            app.score += app.cus3.payment
            #table 4
            if app.server.gridPosition in [[4,5],[4,7]]:     # table 0 , checks if server is in the correct position to take order
                    if app.tables[4].hasCustomer == True: #checks if customer is at table 
                        takeOrder(app.cus4)
            if app.server.gridPosition in [[5,5],[5,7], [6,6]]: #table 0 checks for server next to table to place order   
                if  len(app.server.holding) > 0: 
                        if app.tables[4].order == app.server.holding: #server holding correct Item and presses b
                            app.tables[4].hasPlate = True 
                            app.server.holding = []
                            app.cus4.showOrder = False
                            #customer leaves 
                            app.chair4.empty = True
                            app.cus4.onChair = False 
                            app.tables[4].hasPlate = False
                            app.cus4.arriving = False 
                            app.score += app.cus4.payment
            #table 5
            if app.server.gridPosition in [[4,8]]:     # table 0 , checks if server is in the correct position to take order
                    if app.tables[5].hasCustomer == True: #checks if customer is at table 
                        takeOrder(app.cus5)
            if app.server.gridPosition in [[5,8],[6,9]]: #table 0 checks for server next to table to place order   
                if  len(app.server.holding) > 0: 
                        if app.tables[5].order == app.server.holding: #server holding correct Item and presses b
                            app.tables[5].hasPlate = True 
                            app.server.holding = []
                            app.cus5.showOrder = False
                            #customer leaves 
                            app.chair5.empty = True
                            app.cus5.onChair = False 
                            app.tables[5].hasPlate = False
                            app.cus5.arriving = False 
                            app.score += app.cus5.payment        

def isLegal(app, dir): #checks if server position is going to a table or other object (not including customers)
    [serverRow,serverCol] = app.server.gridPosition
    if dir == "up": 
        if 0 <= serverRow - 1 < app.rows:
            return (app.floor[serverRow -1][serverCol] == None)
        return False #outofbounds
    elif dir == "down": 
        if 0 <= serverRow +1 < app.rows:
            return (app.floor[serverRow + 1][serverCol] == None)
        return False
    elif dir == "left": 
        if 0 <= serverCol -1 < app.cols:
            return (app.floor[serverRow][serverCol - 1] == None)
        return False
    elif dir == "right": 
        if 0 <= serverCol+1  < app.cols:
            return (app.floor[serverRow][serverCol +1] == None)
        return False

def takeOrder(customer): 
    customer.showOrder = True 

def onMousePress(app,mouseX, mouseY): 
    app.breadButton.checkForPress(app, mouseX, mouseY)
    app.lettuceButton.checkForPress(app, mouseX, mouseY)
    app.meatButton.checkForPress(app, mouseX, mouseY)
    app.cutButton.checkForPress(app, mouseX, mouseY)
    app.tutorialButton.checkForPress(app,mouseX, mouseY)

#----------------Button Functions------------------------------------
def addBread(app): # adds bread to counter  
    app.counter.ingredients += ["bread"]
    pass
def addLettuce(app): 
    app.cutting.cutting = True 
    pass
def addMeat(app): 
    app.stove.stoveFull = True
    app.stove = icon("stoveFull", 703, 425 - (app.objectSize //2) )
    app.stove.cooking = True
def cutLettuce(app): 
    if app.cutting.cutting == True: 
        app.cutting.cuttingProgress += 15
        if app.cutting.cuttingProgress >= 56: 
            app.cutting.cutting = False 
            app.counter.ingredients += ["lettuce"]
            app.cutting.cuttingProgress = 1 
    
def onStep(app):
    if not app.gamePaused:
        if app.stove.cooking:
            app.stove.stoveProgress += 20
        if app.stove.stoveProgress >= 56: 
            app.stove = icon("stoveEmpty", 703, 425 - (app.objectSize //2) )
            app.counter.ingredients += ["meat"]
            app.stove.stoveProgress = 0
            app.stove.cooking = False

        if app.cus0.posNum < 11 and app.cus0.arriving: #customer is arriving and is going to sit 
            app.cus0.posNum += 1  
            if app.cus0.posNum == 11: #customer is at chair
                app.cus0.onChair = True
                app.chair0.empty = False 
                app.tables[0].hasCustomer =True 
                app.tables[0].order = app.cus0.order

        if app.cus0.arriving == False and app.cus0.posNum > 0: #customner is leaving 
            app.chair0.empty = True  
            app.cus0.posNum -= 1  
            if app.cus0.posNum == 0:  #customer is at door 
                print(app.cus0.order)
                app.cus0.order = app.cus0.placeFoodOrder() 
                print(app.cus0.order)
                app.cus0.arriving = True 
        
        
        if app.cus1.posNum < 14 and app.cus1.arriving:
            app.cus1.posNum += 1 
            if app.cus1.posNum == 14:
                app.cus1.onChair = True
                app.chair1.empty = False 
                app.tables[1].hasCustomer =True
                app.tables[1].order = app.cus1.order 
        if app.cus1.arriving == False and app.cus1.posNum > 0:
            app.chair1.empty = True 
            app.cus1.posNum -= 1 
            if app.cus1.posNum == 0:
                app.cus1.order = app.cus1.placeFoodOrder()
                app.cus1.arriving = True 
                
        if app.cus2.posNum < 17 and app.cus2.arriving:
            app.cus2.posNum += 1
            if app.cus2.posNum == 17:
                app.cus2.onChair = True
                app.chair2.empty = False 
                app.tables[2].hasCustomer =True 
                app.tables[2].order = app.cus2.order
        if app.cus2.arriving == False and app.cus2.posNum > 0:
            app.chair2.empty = True 
            app.cus2.posNum -= 1 
            if app.cus2.posNum == 0:
                app.cus2.order = app.cus2.placeFoodOrder()
                app.cus2.arriving = True 

        if app.cus3.posNum < 8 and app.cus3.arriving:
            app.cus3.posNum += 1 
            if app.cus3.posNum == 8:
                app.cus3.onChair = True
                app.chair3.empty = False 
                app.tables[3].hasCustomer =True 
                app.tables[3].order = app.cus3.order
        if app.cus3.arriving == False and app.cus3.posNum > 0:
            app.chair3.empty = True 
            app.cus3.posNum -= 1 
            if app.cus3.posNum == 0:
                app.cus3.order = app.cus3.placeFoodOrder()
                app.cus3.arriving = True 

        if app.cus4.posNum < 11 and app.cus4.arriving:
            app.cus4.posNum += 1
            if app.cus4.posNum == 11:
                app.cus4.onChair = True
                app.chair4.empty = False  
                app.tables[4].hasCustomer =True 
                app.tables[4].order = app.cus4.order
        if app.cus4.arriving == False and app.cus4.posNum > 0:
            app.chair4.empty = True 
            app.cus4.posNum -= 1 
            if app.cus4.posNum == 0:
                app.cus4.order = app.cus4.placeFoodOrder()
                app.cus4.arriving = True

        if app.cus5.posNum < 14 and app.cus5.arriving: 
            app.cus5.posNum += 1 
            if app.cus5.posNum == 14:
                app.cus5.onChair = True
                app.chair5.empty = False 
                app.tables[5].hasCustomer =True 
                app.tables[5].order = app.cus5.order
        if app.cus5.arriving == False and app.cus5.posNum > 0:
            app.chair5.empty = True 
            app.cus5.posNum -= 1 
            if app.cus5.posNum == 0:
                app.cus5.order = app.cus5.placeFoodOrder()
                app.cus5.arriving = True 











def main():
    runApp(width=1300,height=800)

main()

def isInside(server,cafe): #server is inside the cafe
    x = server.ThreeDPosition[0] 
    y = server.ThreeDPosition[1]
    #Bounds 
    topX = cafe.TwoDTopLeftPoint[1]
    bottomX = cafe.TwoDTopRightPoint[1]
    topY = cafe.TwoDTopLeftPoint[0]
    bottomY = cafe.TwoDBottomLeftPoint[0] 
    if (topX < x < bottomX) and (topY < y <  bottomY): 
        return True
    return False