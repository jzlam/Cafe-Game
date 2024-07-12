class chef: 
    def __init__(self): #no avatar, just the mouse 
        self.orders = []

    def addOrders(self,order):
        self.orders += order 
    
    def onMousePress(app, mouseX, mouseY):
        pass