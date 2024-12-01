List1 = []
List2 = []
count = 0
with open('hystericalList.txt') as file:
    for i in file:
        val = i.split()
        List1.append(int(val[0]))
        List2.append(int(val[1]))        

for j in range(len(List1)):
    similarity = List1[j] * List2.count(List1[j])
    count += similarity
print(count)
