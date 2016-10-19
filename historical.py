'''
Created on Feb 6, 2016

@author: MsB
'''
import numpy as np
import random

if __name__ == '__main__':
    alpha = 0.1
    
    with open('data.txt') as f:
        data = f.readlines()
    r1 = np.array([float(x.strip('\n')) for x in data])
    r = r1
    mu = np.mean(r)
    var = np.std(r)
    randData = np.random.normal(mu,var,len(r1))
    randData = sorted(randData)
    high = randData[int(len(r1)*(1-float(alpha)/float(2)))]
    low = randData[int(len(r1)*(float(alpha)/float(2)))]
    # b ehtemale 95% dade beine in dotast
    print low , high
    
    count = 0
    for id in r:
#         print id
        if id >= low and id <= high:
            count +=1
    print float(count)/float(len(r))
    
    
