

import math

truncatables = []
num = 11
sum = 0

while len(truncatables) != 11:
    isprime = True
    num += 2
    temp = str(num)
    if int(temp) % 2 == 0:
        isprime = False
    if isprime:
        for i in range(3,int(math.sqrt(num)+1),2):
            if num % i == 0:
                isprime = False
                break
    if isprime:
        for i in range(0,len(temp)-1):
            temp = temp[:-1]
            if int(temp) == 1:
                isprime = False
                break
            for i in range(2,int(math.sqrt(int(temp))+1)):
                if int(temp) % i == 0:
                    isprime = False
                    break
            if not isprime:
                break
    if isprime:
        temp = str(num)
        for i in range(0,len(temp)-1):
            temp = temp[1:]
            if int(temp) == 1:
                isprime = False
                break
            for i in range(2,int(math.sqrt(int(temp))+1)):
                if int(temp) % i == 0:
                    isprime = False
                    break
            if not isprime:
                break
    if isprime:
        truncatables.append(num)
        
for i in range(0,len(truncatables)):
    sum += truncatables[i]
    
print(sum)
