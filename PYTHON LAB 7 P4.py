# Creating an initial tuple
my_tuple = (1, 2, 3)

# Converting the tuple to a list
temp_list = list(my_tuple)

# Adding an item to the list
temp_list.append(4)

# Converting the list back to a tuple
my_tuple = tuple(temp_list)

# Printing the updated tuple
print("Updated tuple:", my_tuple)
