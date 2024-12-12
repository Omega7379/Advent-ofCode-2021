#aoc day 11
# 0 = 1 | even num of digits = even split down middle | else: num * 2024

stones = [64554,35,906,6,6960985,5755,975820,0]
x = 0
while x < 75:
    new_stones = []
    for i in stones:
        print(x)
        if i == 0:
            new_stones.append(1)
        elif (len(str(i))%2 == 0):
            i = str(i)
            first_half = i[:len(i)//2]
            second_half = i[len(i)//2:]
            
            i = int(i)
            new_stones.append(int(first_half))
            new_stones.append(int(second_half))
        else:
            j = i * 2024
            new_stones.append(j)
    stones = new_stones
    
    x += 1

print(len(stones))
