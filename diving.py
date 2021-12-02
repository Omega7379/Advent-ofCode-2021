#Advent of Code day 2, 021221
#Created by Omega7379 | Neiro
#Target: drive the submarine via series of commands from txt file, find distance forward * final depth

#list to track elements of text file
fileRead = ['']

#open and read file
fileRead = open('diveCommands.txt').read().splitlines()

#track distances
up = 0
down = 0
forward = 0

#interate through each piece of the file
for i in range (0, len(fileRead)):
    #element x in file element i
    x = fileRead[i]
    #separate elements of each line in text file
    a,b = x.split(' ')
    #make the number element an int
    b = int(b)

    #if text starts with forward
    if 'forward' in fileRead[i]:
        
        #add value to forward amount
        forward += b

    #if text starts with up
    elif 'up' in fileRead[i]:
        
        #add value to up amount
        up += b

    #or if text starts with down
    elif 'down' in fileRead[i]:

        #add value to down amount
        down += b

#calculate depth ^ distance
depth = down - up
distance = forward * depth

#print to console
print(distance)