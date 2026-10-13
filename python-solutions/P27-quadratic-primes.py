import math

n = -1
isprime = True
product = 0 
primes = 0


for b in range(-1000,1001):
    for c in range(-1000,1001):
        n = -1
        tempp = 0 
        while True:
            isprime =True
            n += 1
            y = n*n+b*n+c
            if (y % 2 == 0 and y != 2) or y < 1:
                break
            for i in range(3,int(math.sqrt(y))+1,2):
                if y % i == 0:
                    isprime = False
                    break
            if not isprime:
                break
            if isprime:
                tempp += 1 
            if tempp > primes:
                primes = tempp
                product = b*c

print(product)
