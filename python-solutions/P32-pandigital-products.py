import math

sum = 0

for i in range(1000,10000):
    nextnum = False
    for j in range(1,100):
        if i % j == 0:
            strnum = str(i) + str(j) + str(i//j)
            if sorted(strnum) == ["1","2","3","4","5","6","7","8","9"]:
                sum += i
                nextnum = True
        if nextnum == True:
            break

print(sum)