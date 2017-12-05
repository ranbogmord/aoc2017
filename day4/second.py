with open("day4/input.txt", "r") as f:
    lines = f.readlines()

correct = len(lines)
for line in lines:
    input_arr = line.strip().split(" ")

    for (k, word) in enumerate(input_arr):
        letters = list(word)
        letters.sort()
        for cmp in input_arr[k+1:]:
            cmp_letters = list(cmp)
            cmp_letters.sort()

            if cmp_letters == letters:
                correct -= 1
                break
        else:
            continue
        break
print(correct)
