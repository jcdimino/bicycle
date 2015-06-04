import random

class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
    def __str__(self):
        return str(self.model) + "$" + str(self.weight * Shop.margin)

        
class Shop(object):
    def __init__(self, name, ):
        self.name = name
        #b self.inventory = inventory dont need this since when you create shop you dont need to pass inventory info into it
        self.inventory = [] #create empty inventory for shop
        self.profit = profit
        
    def __str__(self): #print inventory and profit
        return "Inventory: " + "Profit: " + str(self.profit)
    
   # def price(self, inventory):
        
class Customer(object):
    def __init__(self, name, wallet, bike):
        self.name = name
        self.wallet = wallet
        self.bike = bike
    
    def price_range(self, Shop.cost):
        for price in Shop.cost.iteritems():
            if self.wallet >= price:
                

#creating 6 different bike models
trail = Bicycle("Trail", 10, 100)        
speed = Bicycle("Trail", 10, 150)   
mountain = Bicycle("Trail", 10, 200)   
road = Bicycle("Trail", 10, 300)   
bmx = Bicycle("Trail", 10, 400)   
electric = Bicycle("Trail", 10, 700)   

#create a shop
bike_shop1 = Shop("Billy's Bikes", 0)

#create customers
steve = Customer("Steve", 200, False)
sara = Customer("Sara", 500, False)
jeff = Customer("Jeff", 1000, False)

print(trail)