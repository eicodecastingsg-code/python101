# made with dictionary

menu = {
    "1": ["Hawaiian Pizza", 11.90],
    "2": ["Pepperoni Roni", 13.60],
    "3": ["4 Cheese", 14.40],
    "4": ["Chicken Bonanza", 12.00],
    "5": ["Smoky Mushroom", 8.90],
    "6": ["Fries", 6.50],
    "7": ["Onion Ring", 4.00],
    "8": ["Salad", 7.00],
    "9": ["Coke Zero", 2.00],
    "10": ["Iced Lemon Tea", 1.00],
}



# items() returns all key-value pairs of a dictionary
def display_menu(menu):
    for itemNumber, foodInfo in menu.items():
        print(f"{itemNumber}.", foodInfo[0], f"- ${foodInfo[1]:.2f}")
    print()




def take_order(order):
    while True:
        itemNumber = input("Enter the item you want to order (or 'x' to finish): ")

        if itemNumber == "x":
            break

        # check if it's a valid itemNumber
        if itemNumber not in menu:
            print("Invalid item number. Please try again.")
            continue

        quantity = input("Quantity: ")
        if not quantity.isdigit() or int(quantity) <= 0:
            print("Please enter a valid quantity")
            continue

        # Add to order
        # if the item has already been ordered previously, add up the quantity
        if itemNumber in order:
            order[itemNumber] = int(order[itemNumber])
            order[itemNumber] += int(quantity)
            order[itemNumber] = str(order[itemNumber])
        else:
            # push itemNumber and quantity to order dictionary
            order[itemNumber] = quantity





def order_summary(menu, order):
    print("\n---- Order Summary ----")

    total = 0

    # iterate order dictionary
    for itemNumber, quantity in order.items():
        foodInfo = menu[itemNumber]    # foodInfo is a list!
        foodName = foodInfo[0]
        foodPrice = foodInfo[1]
        foodSubtotal = foodPrice * int(quantity)
        print(f"{foodName} x {quantity} = ${foodSubtotal}")
        total += foodSubtotal

    print(f"\nTotal amount: ${total}")




while True:
    order = {}
    print()
    print("-" * 10 + " Welcome to PizzaRizz " + "-" * 10)
    print()
    display_menu(menu)
    take_order(order)
    order_summary(menu, order)

































