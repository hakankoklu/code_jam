import sys


def fill(case):
    case_str = ''.join([''.join(ii) for ii in case])
    old_case_str = case_str
    while True:
        for ii in range(len(case)):
            for jj in range(len(case[0])):
                if case[ii][jj] == '?':
                    case = fill_cell_vert(ii, jj, case)
        case_str = ''.join([''.join(ii) for ii in case])
        if case_str == old_case_str:
            break
        old_case_str = case_str
    case_str = ''.join([''.join(ii) for ii in case])
    old_case_str = case_str
    while True:
        for ii in range(len(case)):
            for jj in range(len(case[0])):
                if case[ii][jj] == '?':
                    case = fill_cell_hor(ii, jj, case)
        case_str = ''.join([''.join(ii) for ii in case])
        if case_str == old_case_str:
            break
        old_case_str = case_str
    return case


def fill_cell_vert(i, j, case):
    if check_next('up', i, j, case):
        case[i][j] = case[i-1][j]
        return case
    if check_next('down', i, j, case):
        case[i][j] = case[i+1][j]
        return case
    return case


def fill_cell_hor(i, j, case):
    if check_next('left', i, j, case):
        case[i][j] = case[i][j-1]
        return case
    if check_next('right', i, j, case):
        case[i][j] = case[i][j+1]
        return case
    return case


def check_next(direction, i, j, case):
    if direction == 'up':
        return i - 1 >= 0 and case[i - 1][j] != '?'
    if direction == 'left':
        return j - 1 >= 0 and case[i][j-1] != '?'
    if direction == 'down':
        return i + 1 < len(case) and case[i+1][j] != '?'
    if direction == 'right':
        return j + 1 < len(case[0]) and case[i][j+1] != '?'


def read_and_write(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    cases = []
    for ind, line in enumerate(lines):
        if len(line) == 1 and line in '0123456789':
            continue
        case = []
        if ' ' in line:
            row, column = [int(x) for x in line.split(' ')]
            for i in range(row):
                case.append(list(lines[ind + i + 1].strip()))
        if case:
            cases.append(case)
    for ind, case in enumerate(cases):
        print('Case #{}:'.format(str(ind+1)))
        case = fill(case)
        for rr in case:
            print(''.join(rr))
    return cases

read_and_write(sys.argv[1])