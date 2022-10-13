menu = ["chicken pasta", "Egg fried rice", "Egg fried noodles", "Sushi"]

# goal is to see the menu in a formatted way, to allow user to order the meal
for i in menu:
    print(i)

# must be able to order 3 times, with order added to the list
new_order = []

order_length = 3  #max 3 items can be ordered

for food in range(order_length): #loops through the list until correct order length is reached
    item = input("Enter items to order: ")
    new_order.append(item) # allows new item to be added to list

print(new_order) # prints the new order