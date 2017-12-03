# Sets up the data
test_sheet = [
    [5, 9, 2, 8],
    [9, 4, 7, 3],
    [3, 8, 6, 5],
]

# Sets up the sum counter
sum_of_diffs = 0

# Loops through the rows of the data
for row in test_sheet:
    # Loops through the columns in the row
    for k, col in enumerate(row):
        # Loops through all the succeeding columns in the row
        for col2 in row[(k+1):]:
            minCol = min(col, col2) # Fetches the smaller column
            maxCol = max(col, col2) # Fetches the larger column

            # Checks if the larger column is evenly divisible with the smaller one
            if maxCol % minCol == 0:
                # Adds the result of the division to the sum counter
                sum_of_diffs += int(maxCol / minCol)

# Prints the sum
print(sum_of_diffs)
