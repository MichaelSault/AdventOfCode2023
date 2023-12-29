#I didn't feel like parsing the text file and there wasn't a ton of data
#so I just called the function manually today

def findWinConditions(time: int, distance: int) -> int:
    wins = 0
    for i in range(time):
        if ((time-i)*(i)>distance):
            wins += 1
    print("Wins:", wins)
    return wins

#part 1 races
race1 = findWinConditions(62, 553)
race2 = findWinConditions(64, 1010)
race3 = findWinConditions(91, 1473)
race4 = findWinConditions(90, 1074)

print(race1*race2*race3*race4)


#part2
race5 = findWinConditions(62649190, 553101014731074)
print(race5)