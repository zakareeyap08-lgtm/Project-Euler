import math

total = 28
num = 7
factors = 0

while True:
    factors = 0
    num += 1 
    total += num 
    
    for i in range(1,int(math.sqrt(total))):
        if total % i == 0:
            factors += 1
    if factors >= 250:
        print(total)
        break
