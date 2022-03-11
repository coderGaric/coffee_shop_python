class Bar:
    def __init__(self, name):
        self.name = name
        self.milk = 300
        self.water = 300
        self.coffee = 50
        self.order_done = 0

    def __str__(self):
        return self.name

    def prepare_item(self, order):
        ing = order.ingredients

        if not self.check_stock(self.milk, ing["milk"]): 
            self.milk = 300
            print("milk filled")
            
        if not self.check_stock(self.water, ing["water"]): 
            self.water = 300
            print("water filled")
            
        if not self.check_stock(self.coffee, ing["coffee"]): 
            self.water = 300
            print("coffee filled")
        
        self.milk = self.deduct(self.milk, ing["milk"])
        self.water = self.deduct(self.water, ing["water"])
        self.coffee = self.deduct(self.coffee, ing["coffee"])
        self.order_done += 1
        return "Done. Please collect drink at the pick up counter. Thank you."
            
    def check_stock(self, self_x, order_y):
        if self_x > order_y:
            return True
        else: 
            return False

    def deduct(self, x, y):
        return x - y


