#Update set1 by adding items from set2, except common items
# Creating two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Updating set1 by adding items from set2 except common items
set1.update(set2.difference(set1))

# Printing the updated set1
print("Updated set1 by adding items from set2, except common items:", set1)
