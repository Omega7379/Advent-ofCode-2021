List1 = []
List2 = []
total = 0
with open('hystericalList.txt') as file:
    for i in file:
        val = i.split()
        List1.append(int(val[0]))
        List2.append(int(val[1]))        

List1 = sorted(List1)
List2 = sorted(List2)

for j in range(len(List1)):
    difference = abs(List1[j] - List2[j])
    total += difference

print(total)
