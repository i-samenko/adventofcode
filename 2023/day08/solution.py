import numpy as np
import math

data = open('./input.txt', "r").readlines()
instruction = data[0]
nodes = [x.strip() for x in data[2:]]

network = {}
for row in nodes:
    k, v = row.split(' = ')
    network[k] = tuple((v[1:4], v[6:9]))

instruction = [i for i in instruction.strip()]
print(len(instruction), instruction)


curr = 'AAA'
steps = 0
idx = 0

while curr != 'ZZZ':
    direction = instruction[idx % len(instruction)]
    curr = network[curr][{'L': 0, 'R': 1}[direction]]
    idx += 1
    steps += 1
print(steps)


start_nodes = [node for node in network.keys() if node.endswith("A")]
dp = [0] * len(start_nodes)
idx = 0
steps = 0
while 0 in dp:
    for i, node in enumerate(start_nodes):
        if node.endswith("Z") and dp[i] == 0:
            dp[i] = steps
    direction = instruction[idx % len(instruction)]
    start_nodes = [network[node][{'L': 0, 'R': 1}
                                 [direction]] for node in start_nodes]
    idx += 1
    steps += 1

print(math.lcm(*dp))
