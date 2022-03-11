class MenuItem:
    def __init__(self, name, price, cost, ingredients):
        self.name = name
        self.price = price
        self.cost = cost
        self.ingredients = ingredients

    def __str__(self):
        return self.name


class OrderItem(MenuItem):
    def __init__(self, name, price, cost, ingredients, discount=0):
        super().__init__(name, price, cost, ingredients)
        self.discount = discount
        self.sell = round(self.price - (self.price * self.discount), 2)
        self.profit = round(self.sell - self.cost, 2)

    def __str__(self):
        return self.name


