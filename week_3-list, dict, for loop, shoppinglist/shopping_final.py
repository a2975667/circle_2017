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

def calc_price(cart_list, item_dict):
    total_price = 0
    for item in cart_list:
        total_price = total_price + item_dict[item]
    return total_price

def apply_discount(total_price, name, member_dict):
    if (name in member_dict):
        if (member_dict[name] == "gold"):
            final_price = total_price * 0.8
        elif (member_dict[name] == "silver"):
            final_price = total_price * 0.9
        else:
            final_price = total_price * 0.98
    else:
        final_price = total_price
    return final_price

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
total_price = calc_price(cart_list, item_dict)
final_price = apply_discount(total_price, name, member_dict)

if (final_price == 0):
    print("Sorry to see you go without buying anything ;(")
elif (name not in member_dict):
    print("It will be " + "%.2f" % final_price + " HKD.")
else:
    print("It will be " + "%.2f" % final_price + " HKD after discount.")
    print("You save " + "%.2f" % (total_price - final_price) + " dollars!")