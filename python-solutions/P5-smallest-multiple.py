factors = [11,12,13,14,15,16,17,18,19]
num = 20
points = 0 

while True:
    num += 20
    points = 0
    for i in range(0,len(factors)):
        if num % factors[i] == 0:
            points += 1
    if points == len(factors):
        print(num)
        break
