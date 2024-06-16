#Define the menu of hotel
menu = {
    'Pizza':50,
    'Pasta':60,
    'Coffee':40,
    'Tea':20,

}

#greet
print("Welcome to resturant")
print("Pizza:Rs50\nPasta: Rs60\nCoffee: Rs40\nTea: Rs20")

order_total =0

item_1 = input("Enter name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item{item_1} has been added")


else:
    print(f"Ordered item {item_1} is not avaialable yet!")


    another_order = input("Do you want to add another item? (Yes/No) ")
    if another_order == "Yes":
        item_2 = input("Enter name of second item = ")
        if item_2 in  menu:
            order_total += menu[item_2]
            print(f"Item {item_2} has been added")

        else:
            print(f"Order item {item_2} is not avaialble")

print(f"Total amount of order to pay {order_total}")
