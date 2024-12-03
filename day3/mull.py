'''
open file
read line
regex search line

multiply all pairs
add products

repeat
'''
from re import findall

with open('instructions.txt') as file:
    occurence = 0
    string = file.read().strip()
    pattern = findall(r'mul\(\d+,d+\)',string)

    for i in pattern:
        val = list(map(int,i[4:-1].split(",")))
        occurence += val[0] * val[1]
    print(occurence)

    #Part 2 now with do's and do not's
    regex = r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))'
    pattern = findall(regex, string)
    include = True
    occurence_2 = 0

    for j in pattern:
        if j == "do()":
            include = True
        elif j == "don't()":
            include = False
        elif include:
            a = list(map(int, j[4:-1].split(",")))
            occurence_2 += a[0] * a[1]
    print(occurence_2)


