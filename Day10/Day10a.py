# Opens file and reads each line
f = open("c:\\Users\\Michael\\Desktop\\AdventOfCode2023\\Day10\\Day10.txt", "r")

field = []
for y, line in enumerate(f):
    field.append(line)
    curLocation = line.find('S')
    if curLocation >= 0:
        x1, y1 = curLocation, y
x, y, count = x1, y1, 0
if x < len(field[0]) - 1 and field[y][x + 1] in {'-', 'J', '7'}:
    direction = 1
elif y < len(field) - 1 and field[y + 1][x] in {'|', 'J', 'L'}:
    direction = 2

if x > 0 and field[y][x - 1] in {'-', 'F', 'L'}:
    direction = 3
if y > 1 and field[y - 1][x] in {'|', 'F', '7'}:
    direction = 0

while True:
    match direction:
        case 0:
            y -= 1
        case 1:
            x += 1
        case 2:
            y += 1
        case 3:
            x -= 1
    
    match field[y][x]:
        case 'L':
            direction = 1 if direction == 2 else 0
        case 'J':
            direction = 3 if direction == 2 else 0
        case '7':
            direction = 2 if direction == 1 else 3
        case 'F':
            direction = 2 if direction == 3 else 1
    
    count += 1
    
    if x1 == x and y1 == y:
        print(count // 2 + (1 if count % 2 == 1 else 0))
        quit()