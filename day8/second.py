import re

with open("input.txt") as f:
    instructions = f.readlines()
reg = {}
found_max = 0


def get_register_value(register, key):
    if key in register:
        return register[key]
    else:
        return 0


def incr_register_value(register, key, val):
    if key in register:
        register[key] += val
    else:
        register[key] = val

    return register


def decr_register_value(register, key, val):
    if key in register:
        register[key] -= val
    else:
        register[key] = -val

    return register


def parse_instruction(instr):
    regex = re.compile("(.*?)\s(inc|dec)\s(-?\d+)\sif\s(.*?)\s(.*?)\s(-?\d+)")
    matches = regex.match(instr.strip())

    return [
        matches.group(1),
        matches.group(2),
        int(matches.group(3)),
        matches.group(4),
        matches.group(5),
        int(matches.group(6))
    ]


def compare_values(a, op, b):
    if op == "<":
        return a < b
    elif op == ">":
        return a > b
    elif op == "==":
        return a == b
    elif op == "!=":
        return a != b
    elif op == "<=":
        return a <= b
    elif op == ">=":
        return a >= b
    else:
        return False


def find_max(registry):
    max = -999999999
    for item in registry:
        if registry[item] > max:
            max = registry[item]
    return max


def run_instruction(registry, key, op, amount, cmp_key, cmp_op, cmp_val):
    if compare_values(get_register_value(registry, cmp_key), cmp_op, cmp_val):
        if op == "inc":
            registry = incr_register_value(registry, key, amount)
        elif op == "dec":
            registry = decr_register_value(registry, key, amount)

    return registry


for instr in instructions:
    key, op, amount, cmp_key, cmp_op, cmp_val = parse_instruction(instr)

    reg = run_instruction(reg, key, op, amount, cmp_key, cmp_op, cmp_val)
    if find_max(reg) > found_max:
        found_max = find_max(reg)

print(found_max)
