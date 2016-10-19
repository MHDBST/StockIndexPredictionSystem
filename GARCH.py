'''
Created on Feb 5, 2016

@author: MsB
'''
import numpy as np
from scipy import optimize
import statistics as st
from numpy.matlib import rand
 



 
def GARCH11_logL(param, r):
    omega, alpha, beta = param
    n = len(r)
    s = np.ones(n)*0.01
    s[2] = st.variance(r[0:3])
    for i in range(3, n):
        s[i] = omega + alpha*r[i-1]**2 + beta*(s[i-1])  # GARCH(1,1) model
    logL = -((-np.log(s) - r**2/s).sum())
    return logL

def useGarch(om , al , bet):
    sig = st.variance(r)
    r_2 = r[len(r)-1]**2
    return (om+ al * r_2 + bet * sig)
    

if __name__=="__main__":
    alpha = 0.02
    with open('data.txt') as f:
        data = f.readlines()
    r = np.array([float(x.strip('\n')) for x in data])
    o = optimize.fmin(GARCH11_logL,np.array([.1,.1,.1]), args=(r,), full_output=1)
    R = np.abs(o[0])
    
    sig_t = np.sqrt(useGarch(R[0], R[1], R[2]))
    rnd =  np.random.normal(0, 1,1000)
    r_t_all = sig_t*rnd
    r_t = r_t_all[alpha*1000]
   
    count = 0
    for id in r:
#         print id
        if id >=r_t:
            count +=1
    
#     r_t = sorted(r_t)
#     r_t = r_t[50]
print()
print("omega = %.6f\nbeta  = %.6f\nalpha = %.6f\n" % (R[0], R[2], R[1]))

print r_t
print float(count)/float(len(r))

