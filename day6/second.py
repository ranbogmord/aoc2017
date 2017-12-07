# Read the input data
input_data = "4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5".split('\t')
input_data = list(map(lambda x: int(x), input_data))

# input_data = [2, 4, 1, 2]

# Setup variables to store the seen combinations and spent cycles
seen = []
cycles = 0
count_cycles = False

# Run forever
while True:
    # If we've seen the combination, break the loop and finish
    if str(input_data) in seen:
        if count_cycles:
            break
        else:
            seen = []
            count_cycles = True
    else:  # Else add the input to the seen data
        seen.append(str(input_data))

    # Fetch the index of the largest element
    max_index = input_data.index(max(input_data))
    # Fetch the number of blocks to redistribute
    num_to_redistribute = max(input_data)
    # Reset the block to 0
    input_data[max_index] = 0

    # While we still have blocks to redistribute
    while num_to_redistribute > 0:
        # Go to the next index
        max_index = (max_index + 1) % len(input_data)

        # Increment the current memory bank
        input_data[max_index] += 1
        # Decrease the number of blocks to redistribute
        num_to_redistribute -= 1
    if count_cycles:
        # Add 1 to the cycles
        cycles += 1

# Print our final number of cycles
print(cycles - 1)
