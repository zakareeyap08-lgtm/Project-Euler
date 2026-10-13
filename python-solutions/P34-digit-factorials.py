
num = 7*9*8*7*6*5*4*3*2
tempnum = 1
sum = 0
totalnums = 0

for i in range(3,num+1):
    sum = 0
    tempnum = 1
    stri = str(i)
    for j in range(len(stri)):
        for m in range(2,int(stri[j])+1):
            tempnum = tempnum*m 
        sum += tempnum
        tempnum = 1
    if sum == i:
        totalnums += sum

print(totalnums)
