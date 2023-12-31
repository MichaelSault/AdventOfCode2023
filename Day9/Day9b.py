# Opens file and reads each line
f = open("c:\\Users\\Michael\\Desktop\\AdventOfCode2023\\Day9\\Day9.txt", "r")

counter = 0

for x in f:
    history = [[int(m) for m in x.split()]]

    while (len([n for n in history[-1] if n == 0]) < len(history[-1])):
        history.append([history[-1][i + 1] - history[-1][i] for i in range(len(history[-1]) - 1)])

    for i in range(len(history) -2, -1, -1):
        history[i] = [history[i][0] - history[i + 1][0]] + history[i]
    counter += history[0][0]

print ("The new sum of these values is", counter)