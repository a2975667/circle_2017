def welcome_msg():
    print("Welcome!")
    name = input("What is your name? ")
    return name

def print_items(name, item_dict):
    print("Welcome " + name + " :)")
    print("What would you like to buy?")
    for key in item_dict:
        print(key + ": " + str(item_dict[key]) + " HKD")

def add_to_cart(cart_list, item_dict):
    print("Please enter the name of the desired item.")
    while True:
        item = input("Add item? ")
        if (item == "no"):
            break
        elif (item in item_dict):
            cart_list.append(item)
        else:
            print("Sorry, we don't sell " + item + " today. Please re-enter.")

####################################
# this is where the program starts #
####################################

# empty list
cart_list = []
member_dict = {"John": "gold", "Sean": "silver", "Mary": "normal"}
item_dict = {"banana": 2.1, "apple": 3, "shirt": 59.99, "jeans": 199.99, "pen": 10,
             "eraser": 5, "pineapple": 25, "milk": 10, "potato": 2}

name = welcome_msg()
print_items(name, item_dict)
add_to_cart(cart_list, item_dict)