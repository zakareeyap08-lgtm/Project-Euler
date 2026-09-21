
import math

prime = 13
num = 6

while num < 10001:
    isprime = True
    prime += 2 
    for i in range(3, int(math.sqrt(prime) + 1)):
        if prime % i == 0:
            isprime = False
            break
    if isprime:
        num += 1 
    if num == 10001:
        print(prime)
