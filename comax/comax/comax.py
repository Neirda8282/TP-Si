from math import *
from pylab import *
U=[2.475,2.475,2.475,2.475]
I=[4.700,4.900,4.900,4.900]
omegam=[250,75,125,35]
f=(4+1.1)*9.81
v=[108*(10**-3)*(1/60)*omega for omega in omegam]
Pelec=[]
Ps=[]
n=[]
for i in range (len(U)):
    Pelec.append(U[i]*I[i])
    
    Ps.append(v[i]*f)
    n.append(Pelec[i]/Ps[i])
    
plot(Pelec,omegam,'r*',Ps,omegam,'g+',n,omegam,'^')
show()


