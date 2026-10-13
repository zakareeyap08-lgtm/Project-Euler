import math

islychrel = True
sum = 0
count = 0

for i in range(0,10000):
    islychrel = True
    for j in range(0,50):
        if j == 0:
            stri = str(i)
            sum = int(stri) + int(stri[::-1])
            strsum = str(sum)
            if strsum == strsum[::-1]:
                islychrel = False
                break
        else:
            sum = int(strsum) + int(strsum[::-1])
            strsum = str(sum)
            if strsum == strsum[::-1]:
                islychrel = False
                break
        if not islychrel:
            break

    if islychrel:
        count += 1

print(count)
