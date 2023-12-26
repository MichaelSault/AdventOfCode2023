# Opens file and reads each line
f = open("c:\\Users\\Michael\\Desktop\\AdventOfCode2023\\Day4\\Day4.txt", "r")

#define initial values
winCount = 0

for x in f:
    x = x.split(":")[1].split("|")

    #parse for picked and winning numbers
    winning = set([int(m) for m in x[0].strip().split()])
    picked = set([int(m) for m in x[1].strip().split()])
    
    #find cards in both sets
    wins = set(m for m in picked if m in winning)

    if len(wins) > 0:
        winCount += 2**(len(wins)-1)
    
print("The final point count is", winCount)