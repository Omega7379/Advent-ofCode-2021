safe = 0

with open('reports.txt') as file:
    for i in file:
        Up = None
        Us = False
        val = i.split()

        if len(val) < 2:
            safe += 1

        for j in range(len(val)-1):
            if Up == False and int(val[j]) > int(val[j+1]):
                Up = False
            elif Up == None and int(val[j]) < int(val[j+1]):
                Up = True

            if abs(int(val[j]) - int(val[j+1])) >= 1 and abs(int(val[j]) - int(val[j+1])) <= 3:
                if Up and int(val[j]) > int(val[j+1]):
                    Us = True
                    break
                if not Up and int(val[j]) < int(val[j+1]):
                    Us = True
                    break
            else:
                Us = True
                break
        if not Us:
            safe += 1

print(safe)
