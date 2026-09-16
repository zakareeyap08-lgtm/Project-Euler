total = 2
seq = [1,2]

while seq[-1] < 4000001:
    seq.append(seq[-1] + seq[-2])
    if seq[-1] % 2 == 0:
        total += seq[-1]
        
print(total)
