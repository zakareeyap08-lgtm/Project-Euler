import math

num = 0

#9 digits means the largest x value must be of 4 digits as x * 1 = 4 digits then x * 2 = 5 digits
# therfore smallest number must be 5000 and largest is 9999.
for p in range(5000,10000):
    total = str(p) + str(p*2)
    if sorted(total) == ["1","2","3","4","5","6","7","8","9"] and int(total) > num:
        num = int(total)

print(num)