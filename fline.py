import re
bds = input('please enter the name of the data file: ')
di = input('please input the value of d: ')
di = float(di)
#print(di)
kk = input('Please input the iterational times: ')
kk = int(kk)
with open(bds,'r') as f:
     z = f.readlines()
     #print(z)
#print(z)
for i in range(2):
    z[i] = re.split(r'[\s\,]+',z[i].strip())
    print(z[i])
    if z[i][-1] == '':
       z[i].pop()
    print(z[i])
    for j in range(len(z[i])):
        z[i][j] = float(z[i][j])
        print(z[i][j])
            
            
            
        
        
