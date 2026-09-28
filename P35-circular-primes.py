
import math

isprime = True
total = 13

for i in range(101,1000001,2):
    isprime = True
    for j in range(3,int(math.sqrt(i))+1,2):
        if i % j == 0:
            isprime = False
            break
    
    if isprime:
        stri = str(i)
        for z in range(1,len(stri)+1):
            newi = stri[z:] + stri[:z]
            if int(newi) % 2 == 0:
                isprime = False
                break
            for f in range(3,int(math.sqrt(int(newi)))+1,2):
                if int(newi) % f == 0:
                    isprime = False
                    break
            if not isprime:
                break
    
    if isprime:
        total += 1
        
print(total)

