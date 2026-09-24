nums = 0
tempnum =0
pvalue = 0

for p in range(120,1001):
    tempnum = 0
    for a in range(1,p//3):
        for b in range(a+1,(p-a)//2):
            c = p - a - b
            if a*a+b*b==c*c:
                tempnum += 3
    if tempnum > nums:
        nums = tempnum
        pvalue = p
        
print(pvalue)
