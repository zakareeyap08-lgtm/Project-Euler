import math

nums = []
digits = []

def checkprime(num):
    isprime = True
    if num % 2 == 0:
        isprime = False

    if isprime:
        for i in range(3,int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                isprime = False
                break
    return isprime

for n in range(1001,10000,2):
    nums = []
    isjprime = True
    ispermutated = False
    nums.append(n)
    for i in range(1,3):
        nums.append(nums[-1] + 3330)

    for j in range(0,3):
        isjprime = checkprime(nums[j])
        if not isjprime:
            break

    if isjprime:
        if sorted(str(nums[0])) == sorted(str(nums[1])) == sorted(str(nums[2])):
            ispermutated = True
            
    if isjprime and ispermutated:
        total = str(nums[0]) + str(nums[1]) + str(nums[2])
        if len(total) == 12:
            print(total)