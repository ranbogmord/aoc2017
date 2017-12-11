def parse_data(input_data):
    return list(input_data)


def part_two(input_data):
    data = parse_data(input_data)

    total_groups = 0
    depth = 0
    score = 0
    garbage_count = 0
    was_excl = False
    is_garbage = False

    for char in data:
        if was_excl:
            was_excl = False
            continue
        elif char == "!" and is_garbage:
            was_excl = True
        elif char == "<" and not is_garbage:
            is_garbage = True
        elif char == ">":
            is_garbage = False
        elif char == "{" and not is_garbage:
            total_groups += 1
            depth += 1
            score += depth
        elif char == "}" and not is_garbage:
            depth -= 1
        elif is_garbage:
            garbage_count += 1

    return garbage_count


with open("input.txt") as f:
    data = f.read()
    print(part_two(data))
