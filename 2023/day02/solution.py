from functools import reduce


def read_file(file_path):
    with open(file_path, 'r') as file:
        rows = [line.strip() for line in file.readlines()]
    return rows


def check_game(game_line):
    is_possible = True
    gems = {'red': 0, 'green': 0, 'blue': 0}
    for round in game_line.split(';'):
        for gem in round.split(','):
            count, color = gem.strip().split(' ')
            gems[color] = max(int(count), gems.get(color))
            if bag_limit[color] < int(count):
                is_possible = False
    return is_possible, gems


input = read_file('./input-2.txt')
bag_limit = {'red': 12, 'green': 13, 'blue': 14}


sum_id = 0  # part-1
sum_power = 0  # part-2

for game_id, row in enumerate(input, start=1):
    _, game_line = row.split(':')
    is_possible, gems_count = check_game(game_line)
    if is_possible:
        sum_id += game_id
    sum_power += reduce((lambda x, y: x * y), gems_count.values())

print(sum_id, sum_power)
