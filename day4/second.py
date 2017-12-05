# Read input data from file
with open("day4/input.txt", "r") as f:
    # Read lines into list
    lines = f.readlines()

# Create a counter to store the number of correct passphrases
correct = len(lines)
# Go through each passphrase
for line in lines:
    # Split the phrase into a list of words
    input_arr = line.strip().split(" ")

    # Go through each word in the phrase
    for (k, word) in enumerate(input_arr):
        # Split the word into a list of characters
        letters = list(word)
        # Sort the list
        letters.sort()

        # Go through all the following words in the phrase
        for cmp in input_arr[k+1:]:
            # Split the word into a list of chars
            cmp_letters = list(cmp)
            # Sort the list
            cmp_letters.sort()

            # Compare if the original word and the comparison is identical
            if cmp_letters == letters:
                # Decrement the counter
                correct -= 1
                # Break out of the loop
                break
        else:  # Ugly hack
            continue
        break

# Print the answer
print(correct)
