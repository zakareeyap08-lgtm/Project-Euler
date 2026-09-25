
sum = 0

for i in range(1,1000000):
    stri = str(i)
    binary = bin(i)
    temp = str(binary)
    strbin = temp[2:]
    
    if strbin == strbin[::-1] and stri == stri[::-1]:
        sum+= i

print(sum)
