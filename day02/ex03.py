# Password Strength Checker

try:
    userPassword = input("Enter your password: ")
    truePassword = "JustAStudent"

    # check if empty
    if len(userPassword) == 0:
        print(" Password cannot be empty")
    
    # check minimun lenght
    elif len(userPassword) < 12:
        print("Your password too short. minimum 12 characters required.")
    
    #check the correct password
    elif userPassword == truePassword:
        print("Acess granted")
    
    #incorrec password
    else:
        print("Acess denied")

# check invalid input
except ValueError:
    print("Invalid Input")