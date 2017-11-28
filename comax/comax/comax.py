from math import *
from pylab import *
U=[2.475,2.475,2.475,2.475]
I=[4.700,4.900,4.900,4.900]
omegam=[250,75,125,35]

f=(4+1.1)*9.81
#v=[108*(10**-3)*(1/(15.88*60))*omega for omega in omegam]
v=[0.025,0.013,0.008,0.004]
Pelec=[]
Ps=[]
n=[]
Cm=[]
for i in range (len(U)):
    Pelec.append(U[i]*I[i])
    Ps.append(v[i]*f)
    n.append(Ps[i]/Pelec[i])
    Cm.append((0.75*U[i]*I[i])/omegam[i])
   
print(Cm,sum(Cm)/len(Cm))
print(n,sum(n)/len(n))
 
plot(omegam,Pelec,'r*',omegam,Ps,'g+',omegam,n,'^',omegam,Cm,'-')
show()


