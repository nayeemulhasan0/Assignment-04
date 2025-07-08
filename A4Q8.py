import numpy as np
from scipy.optimize import linprog

A = np.array([[-1, -2, 8], [7, 5, -1], [6, 0, 12]])

# Player B (row): maximize v
obj_B = linprog(c=[0, 0, 0, -1],
                A_ub=np.hstack([-A, np.ones((3,1))]),
                b_ub=np.zeros(3),
                A_eq=[[1, 1, 1, 0]],
                b_eq=[1],
                bounds=[(0,None)]*3 + [(None,None)])

# Player A (col): minimize w
obj_A = linprog(c=[0, 0, 0, 1],
                A_ub=np.hstack([A.T, -np.ones((3,1))]),
                b_ub=np.zeros(3),
                A_eq=[[1, 1, 1, 0]],
                b_eq=[1],
                bounds=[(0,None)]*3 + [(None,None)])

print("Player B strategy:", np.round(obj_B.x[:3], 4))
print("Player A strategy:", np.round(obj_A.x[:3], 4))
print("Game value:", round(obj_B.x[3], 4))

