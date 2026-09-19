num = 2 ** 1000
strnum = str(num)
sum = 0

for i in range(len(strnum)):
    sum += int(strnum[i])
    
print(sum)
