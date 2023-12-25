import re

# Opens file and reads each line
f = open("c:\\Users\\Michael\\Desktop\\AdventOfCode2023\\Day2\\Day2.txt", "r")

#define search conditions
setsRegex = "(?<=:)(.*)"
redsRegex = "(\\d+)(?=\\sred)"
greensRegex = "(\\d+)(?=\\sgreen)"
bluesRegex = "(\\d+)(?=\\sblue)"

#define initial values
powerSum = 0

for x in f:
    redMax = 0
    greenMax = 0
    blueMax = 0

    sets = re.search(setsRegex, x).group(0)
    sets = re.split(";", sets)

    for s in sets:
        redCount = re.search(redsRegex, s)
        if (redCount):
            redCount = int(redCount.group(0))
            if(redCount > redMax):
                redMax = redCount

        greenCount = re.search(greensRegex, s)
        if (greenCount):
            greenCount = int(greenCount.group(0))
            if(greenCount > greenMax):
                greenMax = greenCount

        blueCount = re.search(bluesRegex, s)
        if (blueCount):
            blueCount = int(blueCount.group(0))
            if(blueCount > blueMax):
                blueMax = blueCount
        
    power = redMax*greenMax*blueMax
    powerSum += power
    
    
print("The final sum is", powerSum)