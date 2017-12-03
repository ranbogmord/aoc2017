test_sheet = [
    [5, 1, 9, 5],
    [7, 5, 3],
    [2, 4, 6, 8],
]

sum_of_diffs = 0

for row in test_sheet:
    sum_of_diffs += int(max(row)) - int(min(row))

print(sum_of_diffs)
