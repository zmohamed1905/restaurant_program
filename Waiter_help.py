menu = ["chicken pasta", "Egg fried rice", "Egg fried noodles", "Sushi"]

for i in menu:
    print(i)

# must be able to order 3 times, with order added to the list
new_order = []

order_length = 3 #max 3 items can be ordered

for food in range(order_length):
    item = input("Enter items to order: ")
    new_order.append(item)

print(new_order) # prints the new order