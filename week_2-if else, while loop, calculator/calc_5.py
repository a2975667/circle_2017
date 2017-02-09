def welcomeMsg():
    print ("Welcome to calc :)")
    print ("You can: sum, sub, muti, div, factor, compare")
    action = input("what do you want to perform? ")
    return action

# this is where the program starts
action = welcomeMsg()

if (action != "compare"):
    x = eval(input("First number: "))
    y = eval(input("Second number: "))

    if (action == "sum"):
        print (x + " + " + y + " = " + (x+y))

        # why wrong? again, type!
        # print (str(x) + " + " + str(y) + " = " + str(x+y))
        
else:
    print ("do sth")