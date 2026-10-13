
num = 1
sum = 0

for i in range(2, 101):
    num = num * i
    
strnum = str(num)

for i in range(len(strnum)):
    sum += int(strnum[i])
    
print(sum)
