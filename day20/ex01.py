number = int(input("Choose a number: "))
even_count = 0
odd_count = 0
multiply_five = 0

for i in range(1, number + 1):


    if i % 2 == 0:
        even_count += 1
        print(f"Even number: {i}")
    else:
        odd_count += 1
        print(f"Odd number: {i}")

    if i % 5 == 0:
        multiply_five += 1    

print(f"\nTotal even numbers: {even_count}")
print(f"\nTotal Odd numbers: {odd_count}")
print(f"\nMultiple of five: {multiply_five}")