
nums = []
numproduct = 1
dens = []
densproduct = 1

for i in range(10,100):
    for j in range(i + 1,100):
        if i % 10 != 0 :
            stri = str(i)
            strj = str(j)
            if stri[0] == strj[0]:
                stri = stri[1]
                strj = strj[1]
            elif stri[0] == strj[1]:
                stri = stri[1]
                strj = strj[0]
            elif stri[1] == strj[0]:
                stri = stri[0]
                strj = strj[1]
            elif stri[1] == strj[1]:
                stri = stri[0]
                strj = strj[0]
            else:
                strj = 0 
        
            newi = int(stri)
            newj = int(strj)
            if newj != 0:
                if i/j == newi/newj:
                    nums.append(i)
                    dens.append(j)
            
for i in range(0,4):
    numproduct = numproduct*nums[i]
    densproduct = densproduct*dens[i]
    
print(densproduct/numproduct)
    
