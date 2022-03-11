class Counter:
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self._items = []
        self._sales = []
        
    def __str__(self):
        return self.shop_name

    def __len__(self):
        return len(self._items)

    def add_item(self, item):
        self._items.append(item)
    
    def __getitem__(self, index): # iterable
        return self._items[index]

    def __setitem__(self, index, new_item):
        self._items[index] = new_item

    def __delitem__(self, index):
        del self._items[index]

    def list_out_menu(self):
        return "\n".join([f"{index + 1}. {item.name.title()} - price: ${item.price}" \
                for index, item in enumerate(self._items)])

    def find_item(self, name):
        for index, item in enumerate(self._items):
            if item.name == name.lower():
                return f"Available! Please enter {index + 1} to order."
        return "Not in the menu!"

    def order_item(self, order):
        self._sales.append(order)

    def list_out_sales(self):
        return "\n".join([f"{index + 1}. {item.name.title()} - price: ${item.price} - sell: ${item.sell} - cost: ${item.cost} - profit: ${item.profit} " for index, item in enumerate(self._sales)])

    @property
    def num_sales(self):
        return len(self._sales)

    @property
    def total_profit(self):
        return sum([item.profit for item in self._sales])


