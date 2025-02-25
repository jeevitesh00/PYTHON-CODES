#Update the first set with items that don’t exist in the second set
# Creating two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Updating set1 with items that don't exist in set2 (difference)
set1.update(set2.difference(set1))

# Printing the updated set1
print("Updated set1 with items that don't exist in set2:", set1)
