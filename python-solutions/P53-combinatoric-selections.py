import math

count = 0
binomial = 0

for n in range(1,101):
    for r in range(0,n):
        binomial = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

        if binomial > 1000000:
            count += 1

print(count)