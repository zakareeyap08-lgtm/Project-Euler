da = 0
db = 0
sum = 0 

for a in range(1,10001):
    for factors in range(1,a):
        if a % factors == 0:
            da += factors 
    
    for factorsforb in range(1,da):
        if da % factorsforb == 0:
            db += factorsforb
            
    if db == a and db<10000 and da < 10000 and da!= a:
        sum += da
    
    da = 0 
    db = 0 
    
print(sum)
