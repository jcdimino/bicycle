import random

class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

speed = Bycicle("speed", 10, 100)

        "trial": 200,
        "race": 300,
        "road": 400,
        "mountain": 500,
        "electric": 820
            
class Shop(object):
    inventory = {}
    profit = 0
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
    
class Customer(object):
    def __init__(self, name, wallet, bike):
        self.name = name
        self.wallet = wallet
        self.bike = bike

steve = Customer("steve", 200, False)
sara = Customer("sara", 500, False)
jeff = Customer("jeff", 1000, False)

customer_list = [steve, sara, jeff]

# customers = {
#     "steve": ["Steve", 200, False],
#     "sara": ["Sara", 500, False],
#     "jeff": ["Jeff", 1000, False]
# }

stock = {
    "speed": 2,
    "trial": 1,
    "race": 4,
    "road": 8,
    "mountain": 5,
    "electric": 3
}

cust_selection = {
    "steve": [],
    "sara": [],
    "jeff": []
}

for x in customer_list:
    print x.name
    for bike, price in Shop.inventory.iteritems():
        if x.wallet >= price * 1.2:
            cust_selection[x.name].append(bike)
            print "We have %s %s for $%s each" % (str(stock[bike]), bike, str(price * 1.20))
    print ""

# for x in customer_list:
#     while customer_list.bike is not:
#         if 