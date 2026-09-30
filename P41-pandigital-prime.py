
import math

isprime = True
ispandigital = True
num = 0

# largest number is 987654321 
# but sum of any pandigital 9 digit or 8 digit number is always divisilbe by 3 
# 9+8+7+6+5+4+3+2+1 = 45 , 8+7+6+5+4+3+2+1 = 36
for i in range(2143,7654322,2):
    stri = str(i)
    isprime = True
    ispandigital = True
    
    for j in range(1,len(stri)+1):
        if not (str(j) in stri):
            ispandigital = False
            break
        
    if ispandigital:
        for p in range(3,int(math.sqrt(i)+1),2):
            if i % p ==0:
                isprime = False
                break
                
    if ispandigital and isprime and i > num:
        num = i

print(num)
