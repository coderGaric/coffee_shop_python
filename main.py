from shop import MenuItem, OrderItem, Counter, Bar


# --------------- ADMIN SIDE ---------------
initial_drinks = [
    {"name": "latte", "price": 14.95, "cost": 7, "ingredients": {"water": 100, "coffee": 16, "milk": 200}},
    {"name": "cappucino", "price": 15.95, "cost": 8, "ingredients": {"water": 100, "coffee": 20, "milk": 200}},
    {"name": "long black", "price": 12.95, "cost": 5, "ingredients": {"water": 100, "coffee": 40, "milk": 0}},
    {"name": "expresso", "price": 12.95, "cost": 5, "ingredients": {"water": 50, "coffee": 50, "milk": 10}}
]

mocca = MenuItem("mocca", 15.95, 8, {"water": 100, "coffee": 20, "milk": 100})

# create shop and kitchen
cofe_shop = Counter("cofe shop")
cofe_coffee_bar = Bar(f"{cofe_shop}'s coffee bar")

# create menu with add_item(MenuItem())
for drink in initial_drinks:
    cofe_shop.add_item(MenuItem(name=drink["name"], price=drink["price"], cost=drink["cost"], ingredients=drink["ingredients"]))
    
# menu list
print("--------- Intial Menu ----------\n", cofe_shop.list_out_menu(), "\n")

# update item no. 3 with index of 2
cofe_shop[2] = mocca # update / replace with index

# check list after update
print("--------- Menu after update item ----------\n", cofe_shop.list_out_menu(), "\n")

# delete first item
del cofe_shop[0]

# check list after delete
print("--------- Menu after delete item ----------\n", cofe_shop.list_out_menu(), "\n")


# --------------- CUSTOMER ---------------
# check and choose
print(cofe_shop.find_item("moCCa")) # True
print(cofe_shop.find_item("Orange Cordial")) # False 

# order 1
choice_num = 1
choice = cofe_shop[choice_num - 1]
discount_given = 0.1
customer_order = OrderItem(choice.name, choice.price, choice.cost, choice.ingredients, discount_given)
cofe_shop.order_item(customer_order)

# pass order to bar
print(cofe_coffee_bar.prepare_item(customer_order))

# order 2
choice_num = 2
choice = cofe_shop[choice_num - 1]
discount_given = 0
customer_order = OrderItem(choice.name, choice.price, choice.cost, choice.ingredients, discount_given)
cofe_shop.order_item(customer_order)

# pass order to bar
print(cofe_coffee_bar.prepare_item(customer_order))

# order 3
choice_num = 2
choice = cofe_shop[choice_num - 1]
discount_given = 0.15 # 15% discout
customer_order = OrderItem(choice.name, choice.price, choice.cost, choice.ingredients, discount_given)
cofe_shop.order_item(customer_order)

# pass order to bar
print(cofe_coffee_bar.prepare_item(customer_order))


# --------------- ADMIN ---------------
# check sales at the end of day
print("--------- item sold ----------\n", cofe_shop.list_out_sales(), "\n")
print("number of sales: ", cofe_shop.num_sales)
print("profit made: $", cofe_shop.total_profit)

# check order done
print("order done: ", cofe_coffee_bar.order_done)


