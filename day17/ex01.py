# Infinite loop that keeps asking the user for a number
while True:
    
    # Ask the user to choose a number
    # If the user enters 0, the program will stop
    number = int(input("Choose a number: (0 to exit) "))
    print()
    
    # Exit condition
    if number == 0:
        break
    
    # Print the header of the multiplication table
    print("=" * 20 + f"MULTIPLICATION TABLE OF  {number}" + "=" * 20)
    
    # Loop from 1 to 10 to generate the multiplication table
    for i in range(1, 11):
        
        # Print the multiplication result
        # :2 is used to format numbers with a minimum width of 2 characters
        print(f"{i:2} X {number:2} = {i * number}")
    
    # Print a separator line after the table
    print("=" * 50)
    print()


