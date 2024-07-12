from cmu_graphics import *

def onAppStart(app): 
        app.rows = 4 
        app.cols = 4
        app.topX  = 400
        app.topY = 200 
        app.cellHeight = 50
        app.board = [([None] * app.cols) for row in range(app.rows)] 

def redrawAll(app):
        drawBoard(app)

def drawBoard(app):
        for row in range(app.rows):
                for col in range(app.cols):
                        drawParallelogram(app, row,col)

def drawParallelogram(app,row,col):
        drawLine(app.topX, app.topY, app.topX + ((app.cellHeight/2) * (3**.5)), app.topY + 100)
        drawLine(app.topX, app.topY, app.topX - ((app.cellHeight/2) * (3**.5)), app.topY + 100)
        drawLine(app.topX, app.topY + app.cellHeight, app.topX + ((app.cellHeight/2)* (3**.5)), app.topY + app.cellHeight - 100)
        drawLine(app.topX, app.topY + app.cellHeight, app.topX - ((app.cellHeight/2)* (3**.5)), app.topY + app.cellHeight - 100)

def getCellTop(app,row,col):
        cellX = app.topX - ((app.cellHeight/2) * (3**.5)) * row
        cellY = app.topY + (col * 200)
        return (cellX, cellY)


def main():
    runApp(width=800,height=800)

main()