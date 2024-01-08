def read_file(file_path):
    with open(file_path, 'r') as file:
        rows = [line.strip() for line in file.readlines()]
    return rows

data = open('./input.txt', "r").readlines()
data = [x.strip() for x in data]
seeds = [int(x) for x in data[0].split(" ") if x.isdigit()]

maps = []
tempList = []
for i, map in enumerate(data[1:]):
    if map == "":
        maps.append(tempList)
        tempList = []
    else:
        tempList.append(map)
maps.append(tempList)

maps = []
tempList = []
for i, map in enumerate(data[1:]):
    if map == "":
        maps.append(tempList)
        tempList = []
    else:
        tempList.append(map)
maps.append(tempList)

def getDestinations(seeds, map):
    destinations = []
    for i, seed in enumerate(seeds):
        for j, range in enumerate(map):
            mapper = range.split(" ")
            mapper = [int(x) for x in mapper if x.isdigit()]
            if int(seed) >= mapper[1] and seed <= mapper[1] + mapper[2]:
                destinations.append(mapper[0] + int(seed) - mapper[1])
        if len(destinations) == i:
            destinations.append(seed)
    return destinations

for map in maps:
    seeds = getDestinations(seeds, map[1:])
    
seeds2 = []

for i in range(0, len(seeds), 2):
    print(seeds[i], seeds[i+1], seeds[i]+seeds[i+1])
    seeds2.append([x for x in range(seeds[i], seeds[i]+seeds[i+1])])
print(len(seeds2))
