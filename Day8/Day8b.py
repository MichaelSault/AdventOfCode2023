import re
from itertools import cycle
import math

graph = {}
cycles = []

regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'


with open("c:\\Users\\Michael\\Desktop\\AdventOfCode2023\\Day8\\Day8.txt", "r") as f:
    puzzle_input = f.read()

traverse, nodes = puzzle_input.split("\n\n")
traverse = cycle(0 if t == "L" else 1 for t in traverse)

for node, l, r in re.findall(regex, nodes):
    graph[node] = [l, r]

startingNodes = [node for node in graph if node[2] == 'A']

for node in startingNodes:
    for steps, d in enumerate(cycle(traverse), start=1):
        node = graph[node][d]
        if node[2] == 'Z':
            cycles.append(steps)
            break

print ("It took", math.lcm(*cycles), "steps to complete")