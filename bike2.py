import random

class Bicycle:
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
    def __repr__(self):
        return "The {0} bike costs ${1} and weighs {2}lbs".format(self.model, self.price, self.weight)

class BikeShop:
    def __init__(self, name, margin, bikes):
        self.name = name
        self.margin = margin
        self.inventory = {}
        self.profit = 0
        
        for bike in bikes: #create a dictionary of bikes with margin
            bike.price = bike.cost * (1 + self.margin)
            self.inventory[bike.model] = bike
        
    def __repr__(self):
        return "We have: " + str(self.inventory.keys())
        
class Customer:
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.bike = []
        
bike_list = []        
bike_list.append(Bicycle("Trail", 10, 100))
bike_list.append(Bicycle("Speed", 10, 150))
bike_list.append(Bicycle("Mountain", 10, 200))
bike_list.append(Bicycle("Road", 10, 300))
bike_list.append(Bicycle("BMX", 10, 400))
bike_list.append(Bicycle("Electric", 10, 700))

bike_shop = BikeShop("Barry's Bikes", .20, bike_list)

customer_list = []
customer_list.append(Customer("Steve", 200))
customer_list.append(Customer("Sara", 500))
customer_list.append(Customer("Jeff", 1000))

customer_selection = {
    "Steve": [],
    "Sara": [],
    "Jeff": []
}

for customer in customer_list:
    print customer.name + " you can afford:"
    for bike in bike_list:
        if customer.fund >= bike.price:
            customer_selection[customer.name].append(bike)
            print "The {0} bike. It costs ${1}.".format(bike.model, bike.price)
    print '-' * 20
    
print bike_shop

for customer in customer_list:
    purchase = random.choice(customer_selection[customer.name])
    customer.bike.append(purchase.model)
    customer.fund -= purchase.price
    bike_shop.profit += (purchase.price - purchase.cost)
#tried to remove the bike from inventory
    #     for selection in customer_selection.iteritems():
#         if purchase.model in customer_selection.values():
    print "{0}, you bought the {1} bike for ${2}. You still have ${3} left.".format(customer.name, purchase.model, purchase.price, customer.fund)
    
print "{0} has made ${1}".format(bike_shop.name, bike_shop.profit)