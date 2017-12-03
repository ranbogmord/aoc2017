# Number to test
test_num = "1212"

# Convert number to list
test_num_array = list(test_num)

# Initialize sum variable
sum_of_nums = 0

# Calculate the new offset
offset = len(test_num_array) / 2

# Go through all of the digits in the list
for idx, num in enumerate(test_num_array):
    # Fetch the new index based on modulo
    new_idx = (idx + offset) % len(test_num_array)

    # Fetch the number to compare to
    next_num = test_num_array[int(new_idx)]

    # If the two digit matches, add it's value to the sum
    if next_num == num:
        sum_of_nums += int(num)

# Print the result
print(sum_of_nums)
