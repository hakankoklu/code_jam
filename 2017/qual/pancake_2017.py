import sys


def full_flip(pancake_str, flipper_size):
    flip_count = 0
    pancake_list = list(pancake_str)
    for i in range(len(pancake_list) - flipper_size + 1):
        if pancake_list[i] == '-':
            pancake_list = flip_pancakes(pancake_list, i, flipper_size)
            flip_count += 1
        # print(''.join(pancake_list))
    if all([pan == '+' for pan in pancake_list]) == True:
        return flip_count
    return 'IMPOSSIBLE'


def flip_pancakes(pancake_list, ind, size):
    for i in range(ind, ind+size):
        pancake_list[i] = flip(pancake_list[i])
    return pancake_list


def flip(pan):
    if pan == '+':
        return '-'
    return '+'


def read_and_write(file_name):
    with open(file_name) as f:
        next(f)
        case = 1
        for line in f:
            (pancake_str, flipper_size) = line.split(' ')
            flipper_size = int(flipper_size)
            result = full_flip(pancake_str, flipper_size)
            print('Case #{case}: {result}'.format(case=case, result=result))
            case += 1

read_and_write(sys.argv[1])
