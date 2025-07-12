#LPP_min

import numpy as np
from scipy.optimize import linprog

# Coefficients of the objective function (costs/unit)
c = np.array([45, 40, 85, 65])

# Coefficients of the inequality constraints 
A = np.array([
    [ 3,  4,  8,  6],   # F1
    [ 2,  2,  7,  5],   # F2
    [ 6,  4,  7,  4]    # F3
])

b = np.array([ 800,  200,  700])  # Req

# Soln 
result = linprog(c, A_ub=-A, b_ub=-b, method='highs')

# Cout
if result.success:
    print(f"Optimal cost: {result.fun:.2f} BDT")
    print("Optimal units of each food type:")
    print(f"Food Type 1: {result.x[0]:.2f}")
    print(f"Food Type 2: {result.x[1]:.2f}")
    print(f"Food Type 3: {result.x[2]:.2f}")
    print(f"Food Type 4: {result.x[3]:.2f}")
else:
    print("No solution found")

