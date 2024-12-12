stones = [64554, 35, 906, 6, 6960985, 5755, 975820, 0]
x = 0
local_append = stones.append

while x < 75:
    new_stones = []
    local_new_append = new_stones.append  
    local_new_extend = new_stones.extend  
    
    for i in stones:
        i_str = str(i)
        length = len(i_str)
        
        if i == 0:
            local_new_append(1)
        elif length % 2 == 0:
            half = length // 2
            first_half = int(i_str[:half])
            second_half = int(i_str[half:])
            local_new_extend([first_half, second_half])
        else:
            j = i * 2024
            local_new_append(j)
            
    stones = new_stones
    x += 1

print(len(stones))
