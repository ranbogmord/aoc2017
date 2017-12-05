with open("day4/input.txt", "r") as f:
    lines = f.readlines()

correct = 0
for line in lines:
    input_arr = line.strip().split(" ")
    unique_elements = list(set(input_arr))
    if len(input_arr) == len(unique_elements):
        correct += 1

print(correct)
