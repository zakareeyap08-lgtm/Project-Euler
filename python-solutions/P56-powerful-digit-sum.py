import math

sum = 0

for a in range(1,100):
    for b in range(1,100):
        product = a**b
        tempsum = 0
        strproduct = str(product)
        
        for i in range(0,len(strproduct)):
            tempsum += int(strproduct[i])

        if tempsum > sum:
            sum = tempsum

print(sum)