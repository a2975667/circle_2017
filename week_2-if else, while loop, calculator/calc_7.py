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
        print (str(x) + " + " + str(y) + " = " + str(x+y))

    elif (action == "sub"):
        print (str(x) + " - " + str(y) + " = " + str(x-y))

    elif (action == "muti"):
        print (str(x) + " * " + str(y) + " = " + str(x*y))

    elif (action == "div"):
        #answer
        if (y == 0):
            print ("y cannot be 0")
        #print str(x) + " / " + str(y) + " = " + str(float(x)/float(y))
        print (str(x) + " / " + str(y) + " = " + str(x/y))

    elif (action == "factor"):
        print ("do factor")
        
    else:
        print ("cannot define action.")
        
else:
    print ("do sth")