import math

sum = 2
for i in range(3,2000000,2):
    prime = True
    
    for j in range (2, int(math.sqrt(i)) + 1 ):
        if i % j == 0:
            prime = False
            break
        
    if prime:
        sum += i
        
print(sum)
