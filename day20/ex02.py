numbers = []
even_number = 0
odd_number = 0
total_numbers = 0

while True:
    number = int(input("Choose a number (0 to exit): "))
    

    if number == 0:
        print("Goodbye")
        break

    total_numbers += 1  
    numbers.append(number)
    
    if number % 2 == 0:
        even_number += 1
    else:
        odd_number += 1

numbers.sort()

print(f"Total numbers entered: {total_numbers}")
print(f"Even numbers: {even_number}")
print(f"Odd number: {odd_number}")
print(f"largest number: {numbers[-1]}")
print(f"Smallest number: {numbers[0]}")


