# Set aliasing example

# Create a set
original_set = {1, 2, 3, 4, 5}

# Create an alias for the original set
alias_set = original_set

# Display both sets
print("Original Set:", original_set)
print("Alias Set:", alias_set)

# Modify the alias set
alias_set.add(6)

# Display both sets after modification
print("After adding to alias set:")
print("Original Set:", original_set)
print("Alias Set:", alias_set)