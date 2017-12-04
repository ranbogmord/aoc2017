def build_matrix(dim):
    """ Function to build the empty matrix of a given size """
    matrix = []
    for _ in range(dim):
        r = []
        for _ in range(dim):
            r.append(None)
        matrix.append(r)

    return matrix


def calculate_neighbour_sum(coords, matrix):
    """ Calculates the sum of a given cells neighbours """
    nsum = 0
    directions = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]

    for dir in directions:
        if matrix[coords[0] + dir[0]][coords[1] + dir[1]]:
            nsum += matrix[coords[0] + dir[0]][coords[1] + dir[1]]

    return nsum


def get_next_tile(coords, direction):
    """ Returns the next tile given the current coordinates and a direction """
    if direction == 0:
        nx = coords[0] + 1
        ny = coords[1]
    elif direction == 1:
        nx = coords[0]
        ny = coords[1] - 1
    elif direction == 2:
        nx = coords[0] - 1
        ny = coords[1]
    elif direction == 3:
        nx = coords[0]
        ny = coords[1] + 1
    else:
        return coords

    return (nx, ny)


def get_next_direction(current):
    """ Returns the next direction given the current """
    return (current + 1) % 4


def tile_empty(coords, matrix, direction):
    """ Checks if a tile is empty, given the current cell and the direction """
    if direction == 0:
        nx = coords[0] + 1
        ny = coords[1]
    elif direction == 1:
        nx = coords[0]
        ny = coords[1] - 1
    elif direction == 2:
        nx = coords[0] - 1
        ny = coords[1]
    elif direction == 3:
        nx = coords[0]
        ny = coords[1] + 1
    else:
        return False

    if matrix[nx][ny]:
        return False
    else:
        return True


def part2(target):
    """ Sets up the base vars and runs the solution """
    full_matrix = build_matrix(1023)
    current_coords = (512, 512)  # Current coords starts in the middle of the matrix
    full_matrix[current_coords[0]][current_coords[1]] = 1  # Set the first cell to 0
    current_direction = 3  # Begin facing down, required for the loop to work
    current_max = 0  # Stores the max value we've found

    # Run the code until the max is greater than the target
    while target >= current_max:
        if tile_empty(current_coords, full_matrix, get_next_direction(current_direction)):
            # If the tile to the left is empty, change direction one step left
            current_direction = get_next_direction(current_direction)

        # Move one tile forward
        current_coords = get_next_tile(current_coords, current_direction)
        # Calculate the cell value based on the neighbours
        cell_value = calculate_neighbour_sum(current_coords, full_matrix)
        # Set the cell value in the matrix
        full_matrix[current_coords[0]][current_coords[1]] = cell_value

        # Update current max if cell value is larger
        current_max = max(current_max, cell_value)

    return current_max  # finally return the solved value

print(part2(347991))
