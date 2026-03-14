
def sum_number(number):
    total = 0

    for i in range(1, number + 1):
        total += i
    
    return total
    
def square_number(number):
    return number ** 2


def multiply_by_two(number):
    return number * 2
    

def check_number(number):
    return number % 2 == 0




print(square_number(5))
print(multiply_by_two(8))
print(sum_number(8))
print(check_number(5))
print(check_number(8))
