from collections import defaultdict
from functools import reduce


def read_file(file_path):
    with open(file_path, 'r') as file:
        rows = [line.strip() for line in file.readlines()]
    return rows


def is_part(x, y):
    is_part = False
    for row_shift in [-1, 0, 1]:
        for col_shift in [-1, 0, 1]:
            x_shift = x + row_shift
            y_shift = y + col_shift
            if (0 <= x_shift) and (x_shift < rows) and (0 <= y_shift) and (y_shift < cols):
                symbol = engine[x_shift][y_shift]
                if (not symbol.isdigit()) and (symbol != '.'):
                    is_part = True
                if symbol == '*':
                    gears.add((x_shift, y_shift))
    return is_part


def check_value(row_id, symbol_id, symbols='', part_flag=False):
    if symbol_id < cols and engine[row_id][symbol_id].isdigit():
        symbols += engine[row_id][symbol_id]
        if is_part(row_id, symbol_id):
            part_flag = True
        return check_value(row_id, symbol_id+1, symbols, part_flag)
    else:
        symbol_id += 1
    return symbols, part_flag, symbol_id


engine = read_file('./input-3.txt')

rows = len(engine)
cols = len(engine[0])

sum_numbers = 0  # part-1
gears_collection = defaultdict(list)  # part-2


for row_id in range(rows):
    part_flag = False
    symbols = ''
    symbol_id = 0
    gears = set()
    while symbol_id < cols:
        symbols, part_flag, symbol_id = check_value(row_id, symbol_id)
        if part_flag:
            sum_numbers += int(symbols)
            for gear in gears:
                gears_collection[gear].append(int(symbols))
            gears = set()

print(sum_numbers) # part-1
mul_gears = sum([reduce(lambda x, y: x*y, g)
                for g in gears_collection.values() if len(g) > 1])
print(mul_gears) # part-2
