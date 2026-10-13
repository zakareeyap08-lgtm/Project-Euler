strnum = '1234567891011121314151617181920'

for i in range(21,1000000):
    strnum += str(i)
    
print(int(strnum[0]) * int(strnum[9]) * int(strnum[99]) * int(strnum[999]) * int(strnum[9999]) * int(strnum[99999]) * int(strnum[999999]))
