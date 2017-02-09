def welcomeMsg():
    print ("Welcome to calc :)")
    print ("You can: sum, sub, muti, div, factor, compare")
    action = input("what do you want to perform? ")
    return action

# this is where the program starts
action = welcomeMsg()

if (action != "compare"):
    x = input("First number: ")
    y = input("Second number: ")

    print (x + y)

    # why is this wrong?
    # you need to 'eval'
    # https://docs.python.org/2/library/functions.html#eval
    '''
    x = eval(x)
    y = eval(y)
    print (x + y)
    '''

else:
    print ("do sth")