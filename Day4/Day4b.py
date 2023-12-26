import re

# Opens file and reads each line
f = open("c:\\Users\\Michael\\Desktop\\AdventOfCode2023\\Day4\\Day4.txt").read().splitlines()

count = {x: 1 for x in range(1, len(f)+1)}

for x, line in enumerate(f, start=1):
    left, right = line.split(':')[1].split('|')

    winning = {int(number) for number in re.findall(r'\d+', left)}
    picked = {int(number) for number in re.findall(r'\d+', right)}
    matched = len(winning & picked)

    for y in range(x+1, x+1 + matched):
        count[y] += count[x]

print(sum(count.values()))
    
print("The final point count is", sum(count.values()))