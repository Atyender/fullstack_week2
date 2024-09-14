# Demonstrating the difference between extend and append in a list

# Initialize a list
my_list = [1, 2, 3]

# Using append
my_list.append([4, 5])
print("After append:", my_list)  # Output: [1, 2, 3, [4, 5]]

# Resetting the list
my_list = [1, 2, 3]

# Using extend
my_list.extend([4, 5])
print("After extend:", my_list)  # Output: [1, 2, 3, 4, 5]