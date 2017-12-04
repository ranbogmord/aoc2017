def calculate_manhattan_distance(target):
    if target == 1:
        return 0

    dx, dy, c_len = 0, 0, 1
    current_step = 1
    current_corner = 0

    while current_corner < target:
        current_step += 2
        current_corner = current_step ** 2
        dx += 1
        dy += 1

    c_len = current_corner - ((current_step - 2) ** 2)
    while target < current_corner:
        current_corner -= c_len / 4

    diffX = dx
    diffY = abs(abs(target - current_corner) - c_len / 8)

    return int(diffX + diffY)

print(calculate_manhattan_distance(1), " = 0")
print(calculate_manhattan_distance(12), " = 3")
print(calculate_manhattan_distance(23), " = 2")
print(calculate_manhattan_distance(1024), " = 31")
print(calculate_manhattan_distance(347991), " = ?")
