# Creating a tuple with repeated items
my_tuple = (10, 20, 30, 10, 40, 50, 20, 60, 70, 30)

# Finding repeated items using a dictionary to count occurrences
repeated_items = {}
for item in my_tuple:
    if item in repeated_items:
        repeated_items[item] += 1
    else:
        repeated_items[item] = 1

# Printing the repeated items (those with count > 1)
print("Repeated items in the tuple:")
for item, count in repeated_items.items():
    if count > 1:
        print(f"Item {item} is repeated {count} times.")
