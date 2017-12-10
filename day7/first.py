with open('day7/input.txt') as f:
    input_data = f.readlines()

parsed_data = {}
tree = {}
all_children = []


def parse_element(name):
    data = parsed_data[name]
    for idx, child in enumerate(data["children"]):
        if isinstance(child, str):
            data["children"][idx] = parse_element(child)
            all_children.append(child)
    return data


for row in input_data:
    data = row.split(" -> ")

    name = data[0].split(" ").pop(0)
    if len(data) > 1:
        children = data[1].strip().split(', ')
    else:
        children = []

    parsed_data[name] = {
        "name": name,
        "children": children
    }

for key in parsed_data:
    tree[key] = parse_element(key)

for child in all_children:
    del tree[child]

print(list(tree.keys()).pop())
