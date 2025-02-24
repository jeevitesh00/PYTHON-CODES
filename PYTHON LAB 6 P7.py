numbers = [1, 2, 3, 2, 4, 5, 3]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)
