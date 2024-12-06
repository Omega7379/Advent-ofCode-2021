import re
with open('wordsearch.txt') as file:
    occurence = 0
    string = file.read().split('')
    for i in string:
        print(i)

