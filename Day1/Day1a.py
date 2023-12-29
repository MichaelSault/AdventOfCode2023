# Opens file and reads each line
f = open("/Users/michaelsault/Desktop/AdventOfCode2023/Day1/Day1.txt", "r")
c = 0

for x in f:
    a = -1
    b = -1
    for i, char in enumerate(x):
        if char.isdigit():
            if a == -1 :
                a = char
                print('The first number is', a)
            else:
                b = char
    if (b == -1):
        b = a
    print(a, b, c)
    c += int(a+b)
    print(c)

print("The calibration value is", c)
