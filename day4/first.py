# Read input data from file
with open("day4/input.txt", "r") as f:
    # Read lines into list
    lines = f.readlines()

# Create a counter to store the number of correct passphrases
correct = 0
# Go through each passphrase
for line in lines:
    # Split the phrase into a list of words
    input_arr = line.strip().split(" ")
    # Get a list of all the unique elements in the word list
    unique_elements = list(set(input_arr))

    # Compare the length of the original word list and
    # the list of unique elements
    if len(input_arr) == len(unique_elements):
        # Increment the correct counter if the lengths match (only unique elements)
        correct += 1

# Print the answers
print(correct)
