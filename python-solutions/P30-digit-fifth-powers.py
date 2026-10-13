
num = 6*(9**5)
sum = 0
total = 0

for i in range(2,num+1):
    sum = 0
    stri = str(i)
    for j in range(len(stri)):
        sum += int(stri[j])**5
    if sum == i:
        total += sum
print(total)
