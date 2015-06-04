class Bicycle:
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

#        self.in_store_count = 0
    def __str__(self):
        return "The {0} costs ${1} and weighs {2}lbs.".format(self.model, self.cost, self.weight)

class BikeShopPrivateBikeInfo:
    
class BikeShop:
    def __init__(self, name, margin, bikes):
        self.name = name
        self.margin = margin
        
        products = {}

        for bike in bikes:
            new_product = BikeShopPrivateBikeInfo ()
            new_product.bike = bike
            new_product.price = bike.cost * margin
            new_product.inventory = 0
            products[bike.model] = new_product
        
    def add_to_inventory(self, model_name, added_count):
        product = products.get(model_name)
        product.inventory += added_count
        
class Customer:
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.bike = None
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#creating 6 different bike models
trail = Bicycle("Trail", 10, 100)        
speed = Bicycle("Speed", 10, 150)   
mountain = Bicycle("Mountain", 10, 200)   
road = Bicycle("Road", 10, 300)   
bmx = Bicycle("BMX", 10, 400)   
electric = Bicycle("Electric", 10, 700)   

bikes = [trail, speed, mountain, road, bmx, electric] #isntead append this

#create a shop
bike_shop1 = BikeShop("Billy's Bikes", 20, bikes)

bike_shop1.add_to_inventory("Electric", 12)

#create customers
steve = Customer("Steve", 200, False)
sara = Customer("Sara", 500, False)
jeff = Customer("Jeff", 1000, False)

customers = [steve, sara, jeff]