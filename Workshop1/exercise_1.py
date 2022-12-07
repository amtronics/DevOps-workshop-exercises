import typing


def basic_calc(op: str, a: int, b: int) -> typing.Union[float, int]:
    if op == 'x':
        return a*b
    elif op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '/':
        return a/b
    else:
        raise Exception("invalid operator")


def parse_line_step3(line: str) -> int:
    ''' Returns line number to go to'''
    items = line.split()
    if len(items) == 2:
        return int(items[1])
    else:
        return int(basic_calc(items[2], int(items[3]), int(items[4])))


def parse_line_step4(line: str, data_lines) -> typing.Optional[int]:
    ''' Returns line number to go to or None'''
    items = line.split()
    if items[0] == "goto":
        if items[1] == 'calc':
            return int(basic_calc(items[2], int(items[3]), int(items[4])))
        else:
            return int(items[1])
    elif items[0] == "replace":
        # replace
        data_lines[int(items[1])-1], data_lines[int(items[2])-1] = data_lines[int(items[2])-1], data_lines[int(items[1])-1]
        return None
    elif items[0] == "remove":
        # remove
        del data_lines[int(items[1])-1]
        return None
    else:
        return None


def step_2(data_lines):
    sum = 0.0
    for line in data_lines:
        act, op, a, b = line.split()
        sum += basic_calc(op, int(a), int(b))
    return sum


def step_3(data_lines):
    seen_lines: typing.List[str] = []
    index = 0
    while True:
        if data_lines[index] in seen_lines:
            break
        seen_lines.append(data_lines[index])
        index = parse_line_step3(data_lines[index])

    return (data_lines[index], index+1)


def step_4(data_lines):
    seen_lines: typing.List[str] = []
    index = 0
    max_index = len(data_lines) - 1
    while True:
        if index > max_index:
            break
        if data_lines[index] in seen_lines:
            break
        seen_lines.append(data_lines[index])
        ret = parse_line_step4(data_lines[index], data_lines)
        if ret:
            index = ret
        else:
            index += 1

    return (data_lines[index], index+1)


if __name__ == "__main__":   

    with open("Workshop1/step_2.txt", 'rt') as f:
        data_lines = [line.strip() for line in f if line.strip() != '']
        print(f"step2: {step_2(data_lines)}")

    with open("Workshop1/step_3.txt", 'rt') as f:
        data_lines = [line.strip() for line in f if line.strip() != '']
        print(f"step3: {step_3(data_lines)}")

    with open("Workshop1/step_4.txt", 'rt') as f:
        data_lines = [line.strip() for line in f if line.strip() != '']
        print(f"step4: {step_4(data_lines)}")

