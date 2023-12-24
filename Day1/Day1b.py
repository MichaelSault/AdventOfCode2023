# Opens file and reads each line
f = open("/Users/michaelsault/Desktop/AdventOfCode2023/Day1/Day1.txt", "r")
c = 0

str2int = {
    "zero": "z0o",
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

def replace_words(text):
    for k, v in str2int.items():
        text = text.replace(k,v)
    return text

for x in f:
    a = -1
    b = -1
    y = replace_words(x)
    print(x)
    print(y)
    for i, char in enumerate(y):
        if char.isdigit():
            if a == -1 :
                a = char
            else:
                b = char
    if (b == -1):
        b = a
    print(a, b, c)
    c += int(a+b)
    print(c)

print("The calabration value is", c)
