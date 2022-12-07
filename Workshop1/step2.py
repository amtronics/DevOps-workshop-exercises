import typing

def step_2(data_lines):
    sum = 0.0
    for line in data_lines:
        act, op, a, b = line.split()
        sum += basic_calc(op, int(a), int(b))
    return sum
