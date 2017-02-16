def welcome_msg():
    print("Welcome!")
    print("What is your name?")
    name = input()
    return name

def print_items(name, item_dict):
    print("Welcome " + name + " :)")
    print("What would you like to buy?")
    for key in item_dict:
        print(key + ": " + str(item_dict[key]) + " HKD")

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