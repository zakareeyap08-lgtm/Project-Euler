nums = [89,144]
index = 12
strnum = str(nums[-1])

while len(strnum) < 1000:
    nums.append(nums[-1]+nums[-2])
    nums.pop(0)
    index += 1
    strnum = str(nums[-1])
    
print(index)
