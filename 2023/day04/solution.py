def read_file(file_path):
    with open(file_path, 'r') as file:
        rows = [line.strip() for line in file.readlines()]
    return rows


total_points = 0  # part - 1
cards = {}  # part - 2
for card_id, row in enumerate(read_file('./input-4.txt'), start=1):
    if card_id not in cards:
        cards[card_id] = 1
    _, num_line = row.split(':')
    nums, win_nums = num_line.split('|')
    matches = set(nums.split()) & set(win_nums.split())
    total_points += 2**(len(matches)-1) if len(matches) > 0 else 0
    for n in range(card_id, card_id + len(matches)):
        cards[n] = cards.get(n, 1) + cards[card_id-1]


print(total_points)
print(sum(cards.values()))