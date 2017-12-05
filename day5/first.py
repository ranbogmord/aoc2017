# Read input stack
with open("day5/input.txt", "r") as f:
    # Parse the lines and format
    stack = list(map(lambda x: int(x.strip()), f.readlines()))

# Set initial index to 0
current_idx = 0
# Set initial step count to 0
steps = 0

try:
    # Run forever
    while True:
        # Store the new index temporarily based on the value of the cell
        new_idx = current_idx + stack[current_idx]
        # Increment the current cell value by one
        stack[current_idx] += 1
        # Set the current index to the new index
        current_idx = new_idx
        # Increment the steps by one
        steps += 1
except IndexError as ex:  # Catch IndexError's (trying to go outside the list)
    # Print the number of steps taken (answer)
    print(steps)
