def calculate_manhattan_distance(target):
    if target == 1:
        return 0  # Return 0 if target is 1

    dx, dy, c_len = 0, 0, 1  # Setup base variables, dy is probably unnecessary
    current_step = 1  # Current step (column) from origin
    current_corner = 0  # Current corner value

    while current_corner < target:  # Find the first corner larger than our target
        current_step += 2  # Increase col by 2, we only need to find the uneven perfect squares
        current_corner = current_step ** 2  # Calculate the perfect square of the current step
        dx += 1  # increase dx
        dy += 1  # increase dy

    c_len = current_corner - ((current_step - 2) ** 2)  # Calculate the length of the outer ring
    while target < current_corner:  # Find the closest corner smaller than our target
        current_corner -= c_len / 4  # Switch corner to the next smaller one

    # Set the diff in one direction to dx
    diffX = dx

    # Set the diff in the other direction to the distance to the corner
    diffY = abs(abs(target - current_corner) - c_len / 8)

    return int(diffX + diffY)  # Return the sum of the distances

print(calculate_manhattan_distance(1), " = 0")
print(calculate_manhattan_distance(12), " = 3")
print(calculate_manhattan_distance(23), " = 2")
print(calculate_manhattan_distance(1024), " = 31")
print(calculate_manhattan_distance(347991), " = ?")
