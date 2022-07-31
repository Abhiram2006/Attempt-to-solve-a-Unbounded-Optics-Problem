import numpy as np
def minv(f1, f2, u):
    return ((f1+u)*(f2-10+(u*f1)/(u+f1)))/(f1*f2)
def udd(u,f1, f2):
    return f2*((u*f1/(u+f1))-10)/(f2+(u*f1)/(u+f1)-10)
def v(f1, f2, u):
    return (minv(f1, f2, u)**(-2))*np.abs((udd(u,f1, f2)-udd(-2, f1, f2))/(u+2))
def V(u, f1, f2):
    return (1/(3*(u+2)))*((u*f1)/(u+f1)+(2*f1)/(-2+f1))*((f1/(f1-2))**2+(f1/(f1+u))**2+(f1/(f1+u))*(f1/(f1-2)))
def f(u, f1, f2):
    return ((minv(f1, f2,u)-minv(f1, f2,-2))/minv(f1, f2,-2))**2+((v(f1, f2, u)/500)-1)**2
import matplotlib.pyplot as plt
import math
N=1
u1=-2
u2=-3
l=0.5*10**(-1)
# l1=1*10**(-1)
d=1*10**(-8)
n=100000
VL=[]
uL=[]
for i in range(N):
    u=u1+(u2-u1)*((i+1)/N)
    f1=7
    f2=16.5
    for j in range(n):
        fb=(f(u, f1+d, f2)-f(u, f1, f2))/d
        fc=(f(u, f1, f2+d)-f(u, f1, f2))/d
        
        F=(math.sqrt(fb**2+fc**2))**(0.5)
        
        f1-=fb*l/F
        f2-=fc*l/F
        print(' f1= ',f1,' f2= ',f2,' u=',u,' fb= ',fb,' fc= ',fc)
    
    VL.append(V(u, f1, f2))
    uL.append(u)
    print('loop ended')
    print((minv(f1, f2,u)-minv(f1, f2,-2))/minv(f1, f2,-2), (v(f1, f2, u)-500)/500, ' f1= ',f1,' f2= ',f2,' u=',u)

 

plt.plot(uL, VL)
plt.show()
    
Fb=[]
F1=[]
f11=3.1914875
f12=3.19149
N=1000
u=-3
f2=60
for i in range(N):
    f1=f11+(f12-f11)*((i+1)/N)
    fb=(f(u, f1+d, f2)-f(u, f1, f2))/d
    Fb.append(fb)
    F1.append(f1)
plt.plot(F1,Fb)
plt.show()

Fc=[]
F2=[]
f21=1
f22=100
N=1000
u=-3
f1=60
for i in range(N):
    f2=f21+(f22-f21)*((i+1)/N)
    fc=(f(u, f1, f2+d)-f(u, f1, f2))/d
    Fc.append(fc)
    F2.append(f2)
plt.plot(F2,Fc)
plt.show()
