def welcomeMsg():
    print ("Welcome to calc :)")
    print ("You can: sum, sub, muti, div, factor, compare")
    action = input("what do you want to perform? ")
    return action

def calculation(action, x, y):
    if (action == "sum"):
        print (str(x) + " + " + str(y) + " = " + str(x+y))
        return (x+y)

    elif (action == "sub"):
        print (str(x) + " - " + str(y) + " = " + str(x-y))
        return (x-y)

    elif (action == "muti"):
        print (str(x) + " * " + str(y) + " = " + str(x*y))
        return (x*y)

    elif (action == "div"):
        if (y == 0):
            print ("y cannot be 0")
            return -1
        print (str(x) + " / " + str(y) + " = " + str(x/y))
        return (x/y)

    elif (action == "factor"):
        if (x % y == 0):
            print (str(y) + " is a factor of " + str(x))
            return -1
        else:
            print (str(y) + " is not a factor of " + str(x))
            return -1
        
    else:
        print ("cannot define action.")
        return -1

# this is where the program starts
action = welcomeMsg()

if (action != "compare"):
    x = eval(input("First number: "))
    y = eval(input("Second number: "))

    res = calculation(action, x, y)

else:
    act1 = input("First action: ")
    x1 = eval(input("First number: "))
    y1 = eval(input("Second number: "))
    act2 = input("Second action: ")
    x2 = eval(input("First number: "))
    y2 = eval(input("Second number: "))

    res1 = calculation(act1, x1, y1)
    res2 = calculation(act2, x2, y2)  
    