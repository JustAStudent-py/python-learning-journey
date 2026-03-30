def verify_numbers(numbers):
    count_dict = {}

    # Count occurrences (only 1 loop)
    for n in numbers:
        if n in count_dict:
            count_dict[n] += 1
        else:
            count_dict[n] = 1

    duplicates = []
    unique_numbers = []

    # Classify numbers
    for n, count in count_dict.items():
        if count == 1:
            unique_numbers.append(n)
        else:
            duplicates.append(n)

    return duplicates, unique_numbers, count_dict


numbers = [1, 2, 2, 3, 4, 4, 4, 5]
print(verify_numbers(numbers))