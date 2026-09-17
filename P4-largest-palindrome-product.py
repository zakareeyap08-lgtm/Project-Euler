num = 0
palindrome = 0
for i in range(100,1000):
    for j in range(100,1000):
        num = i*j
        numstr = str(num)
        
        if (numstr == numstr[::-1]) and (num > palindrome):
            palindrome = num
            
print(palindrome)
