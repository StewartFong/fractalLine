import re
import pylab as pl
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
    #print(z[i])
    if z[i][-1] == '':
       z[i].pop()
    #print(z[i])
    for j in range(len(z[i])):
        z[i][j] = float(z[i][j])
        #print(z[i][j])
x = z[0]
y = z[1]
xl = x[-1]-x[0]
pl.plot(x,y)
pl.show() 
n = len(x)
nn = n-1
a = []
e = []
c = []
f = []
xx = []
yy = []
for k in range(kk):
    for i in range(nn):
        a.append((x[i+1]-x[i])/xl)
        e.append((x[-1]*x[i]-x[0]*x[i+1])/xl)
        c.append((y[i+1]-y[i]-di*(y[-1]-y[0]))/xl)
        f.append(((x[-1]*y[i]-x[0]*y[i+1])-di*(x[-1]*y[0]-x[0]*y[-1]))/xl)
    for i in range(nn):
        for j in range(n):
            xx.append(a[i]*x[j]+e[i])
            yy.append(c[i]*x[j]+di*y[j]+f[i])
    n = len(xx)
    nn = n-1
    x = xx
    y = yy
    xx = []
    yy = []
    a = []
    e = []
    c = []
    f = []
pl.plot(x,y)
pl.show()
with open('%sI%d.result'%(bds,kk),'w') as f:
     for i in range(len(x)):
         f.write('(%f,%f)'%(x[i],y[i]))

            
            
        
        
