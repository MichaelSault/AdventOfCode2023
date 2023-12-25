import re

# Opens file and reads each line
f = open("c:\\Users\\Michael\\Desktop\\AdventOfCode2023\\Day2\\Day2.txt", "r")

#define search conditions
gameIDRegex = "(\\d+(?=:))"
setsRegex = "(?<=:)(.*)"
redsRegex = "(\\d+)(?=\\sred)"
greensRegex = "(\\d+)(?=\\sgreen)"
bluesRegex = "(\\d+)(?=\\sblue)"

#define initial values
gameNumberSum = 0

for x in f:
    possible = True
    gameNumber = int(re.search(gameIDRegex, x).group(0))
    sets = re.search(setsRegex, x).group(0)
    sets = re.split(";", sets)

    for s in sets:
        redCount = re.search(redsRegex, s)
        if (redCount):
            redCount = int(redCount.group(0))
            if(redCount > 12):
                possible = False

        greenCount = re.search(greensRegex, s)
        if (greenCount):
            greenCount = int(greenCount.group(0))
            if(greenCount > 13):
                possible = False

        blueCount = re.search(bluesRegex, s)
        if (blueCount):
            blueCount = int(blueCount.group(0))
            if(blueCount > 14):
                possible = False
        
    if(possible):
        gameNumberSum += gameNumber
        print(gameNumber)
        print(gameNumberSum)
    
print("The final sum is", gameNumberSum)