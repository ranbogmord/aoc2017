import re, json

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


def calculate_tower_weight(element):
    w = element['weight']
    if len(element["children"]) > 0:
        for child in element["children"]:
            w += int(calculate_tower_weight(child))
    return w


def calculate_tower_weight_with_print(element, iteration=0):
    w = element['weight']
    if len(element["children"]) > 0:
        for child in element["children"]:
            w += int(calculate_tower_weight_with_print(child, iteration+1))
    print("%s%s %s %s" % ('  ' * iteration, element["name"], element["weight"], w))
    return w


regex = re.compile("(.*)?\s\((\d+)\)")
for row in input_data:
    data = row.split(" -> ")

    matches = regex.match(data[0])
    name = matches.group(1)
    weight = int(matches.group(2))
    if len(data) > 1:
        children = data[1].strip().split(', ')
    else:
        children = []

    parsed_data[name] = {
        "name": name,
        "weight": weight,
        "children": children
    }

for key in parsed_data:
    tree[key] = parse_element(key)

for child in all_children:
    del tree[child]

root_key = list(tree.keys()).pop()
for el in tree[root_key]["children"][4]["children"][1]["children"]:
    print(el["name"], el["weight"], calculate_tower_weight(el))
