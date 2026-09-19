finalchain = 1
chain = 0
num = 0
finalnum = 0

for i in range (1000000,1,-1):
    num = i
    chain = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3*num + 1 
        chain += 1 
    if chain > finalchain:
        finalchain = chain
        finalnum = i
        
print(finalnum)
