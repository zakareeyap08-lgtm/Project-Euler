
num = 600851475143
factor = 2

while num % factor == 0:
    num = num / 2
    
factor = 3

while factor**2 <= num:
    while num % factor == 0:
        num = num / factor
    else:
        factor += 2
        
print(num)
