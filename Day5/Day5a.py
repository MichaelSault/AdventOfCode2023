import re

# Opens file and reads each line
f = open("c:\\Users\\Michael\\Desktop\\AdventOfCode2023\\Day5\\Day5.txt").read().splitlines()

maps =[]

for x in f[2:]:
    if 'map' in x:
        maps.append(dict())
    elif x != '':
        end, start, length = [int(value) for value in x.split()]
        maps[-1][range(start, start+length)] = range(end, end+length)

def findLocation(start: int) -> int:
    value = start
    for curMap in maps:
        value = next(
            (endRange.start + (value - startRange.start)
            for startRange, endRange in curMap.items()
            if value in startRange),
            value
        )
    return value

seeds = [int(seed) for seed in re.findall(r'\d+', f[0])]
locations = [findLocation(seed) for seed in seeds]

print(min(locations))