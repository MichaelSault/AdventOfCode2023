import re
from itertools import cycle
import math

with open("c:\\Users\\Michael\\Desktop\\AdventOfCode2023\\Day8\\Day8.txt", "r") as f:
    puzzle_input = f.read()

traverse, nodes = puzzle_input.split("\n\n")

traverse = cycle(0 if t == "L" else 1 for t in traverse)
graph = {}

regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'

for node, l, r in re.findall(regex, nodes):
    graph[node] = [l, r]

node = 'AAA'

for steps, t in enumerate(traverse, start=1):
        node = graph[node][t]
        print(node)
        if node == 'ZZZ':
            print("node reached")
            break

print ("It took", steps, "steps to complete")