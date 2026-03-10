print("WELCOME TO PEPE'S PIRI PIRI")
print("----------------------------")
print("What would you like to order?")

menu = {"Prime Pita":4.79,
        "Chicken XL":4.79,
        "The Wrap":4.79,
        "BBQ Sizzler":4.99,
        "Chicken n Rice":5.99,
        "Chinese Laksa Noodles":5.99,
        "Chicken Tasca":5.49,
        "Chicken Burrito":4.99,}

order_list = []

flavour = ["Mild", "Hot","Extreme Hot"]
fries = ["Plain Fries", "Peri Peri Fries"]
drinks = ["Pepsi","Pepsi Max","7UP","Tango","Redbull","Rubricon"]
dip = ["Garlic Mayo Dip","Peri Peri Mayo Dip","Sweet Chilli Dip","Extreme Hot Dip"]

#TAKING ORDERS
def take_order():
    order_details = {}

    print("\nMENU")
    print("----------------------")

    for dishes in menu:
        print(dishes, f"£{menu[dishes]}", sep="\t")
    order = input("Place your order here: ")

    while order not in menu:
        print("Item not found. Please choose from the menu.")
        order = input("Place your order here: ")

    order_details["item"] = order

    for item_flavour in flavour:
        print(item_flavour)
    flavour_choice = input("Which flavour would you like? ")
    order_details["flavour"] = flavour_choice

    meal = input(f"You want {order} as a meal? (Yes/No)\n")
    order_details["meal"] = meal

    if meal.lower() == "yes":
        for fries_flavour in fries:
            print(fries_flavour)
        fries_choice = input("Which fries would you like? ")
        order_details["fries"] = fries_choice

        for drinks_flavour in drinks:
            print(drinks_flavour)
        drinks_choice = input("Which drink would you want? ")
        order_details["drink"] = drinks_choice

    for dip_flavour in dip:
        print(dip_flavour)
    dip_choice = input("Which dip you want: ")
    order_details["dip"] = dip_choice

    return order_details

while True:
    order_details = take_order()
    if order_details:
        order_list.append(order_details)

    other_orders = input("Anything else? (Yes/No) ")
    if other_orders.lower() != "yes":
        break

#RECEIPT
print("\n----------------------")
print("   PEPE'S PIRI PIRI")
print("       RECEIPT")
print("----------------------")

print("Item List:")
for i in order_list:
    print(f"Item: {i['item']}, Flavour: {i['flavour']}, Meal: {i['meal']}", end="")
    if i['meal'].lower() == "yes":
        print(f", Fries: {i['fries']}, Drink: {i['drink']}", end="")
    print(f", Dip: {i['dip']}")

print("----------------------")

Total_price = 0
for order in order_list:
    item_price = menu[order["item"]]
    if order["meal"].lower() == "yes":
        item_price += 1.80
    Total_price += item_price

print(f"TOTAL: £{Total_price:.2f}")
print("Thank you for visiting!")



