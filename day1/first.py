# Number to test
test_num = "1122"

# Convert number to list
test_num_array = list(test_num)

# Initialize sum variable
sum_of_nums = 0

# Go through all of the digits in the list
for idx, num in enumerate(test_num_array):
    # Check if we're on the last digit
    if idx == len(test_num_array) - 1:
        # Set the number to compare to the first digit
        next_num = test_num_array[0]
    else:
        # Else set the number to compare to the next digit
        next_num = test_num_array[idx + 1]

    # If the two digit matches, add it's value to the sum
    if next_num == num:
        sum_of_nums += int(num)

# Print the result
print(sum_of_nums)
