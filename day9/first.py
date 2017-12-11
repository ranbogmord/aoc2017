def parse_data(input_data):
    return list(input_data)


def part_one(input_data):
    data = parse_data(input_data)

    total_groups = 0
    depth = 0
    score = 0
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

    return score


with open("input.txt") as f:
    data = f.read()
    print(part_one(data), "?")
