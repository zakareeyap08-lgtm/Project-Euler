nums = 0
tempnum =0
pvalue = 0

for p in range(120,1001):
    tempnum = 0
    for a in range(1,p-1):
        for b in range(1,p-a):
            c = p - a - b
            if a+b+c==p and a*a+b*b==c*c:
                tempnum += 3
    if tempnum > nums:
        nums = tempnum
        pvalue = p
        
print(pvalue)
