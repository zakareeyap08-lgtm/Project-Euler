sum = 0
sqsum = 0
for i in range(1,101):
    sum += i
    sqsum += i*i
    
sum = sum*sum

print(sum - sqsum)
