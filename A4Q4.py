import numpy as np
from scipy.optimize import linprog

M=1e6
c=[4,3,0,0,0,M,M,M]

A=np.array([
    [200,100,-1,0,0,1,0,0],
    [1,2,0,-1,0,0,1,0],
    [40,40,0,0,-1,0,0,1]
])

b=np.array([4000,50,1400])

result=linprog(c,-A,-b,method='simplex')

for i in range(2):
    print(f" food {i+1} : {result.x[i]} unit" )

print(f"optimal cost : {result.fun} tk ")
