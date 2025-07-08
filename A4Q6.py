import numpy as np
import pandas as pd
from scipy.optimize import linprog

# Data
factories   = ['F1', 'F2', 'F3']
warehouses  = ['W1', 'W2', 'W3']
cost_matrix = np.array([[16, 20, 12],
                        [14,  8, 18],
                        [26, 24, 16]])
cost = cost_matrix.flatten()

supply = [200, 160,  90]
demand = [180, 120, 150]

# faka tray
A_ub, b_ub = [], []

# Supply constraints: sum_j x[i,j] ≤ supply[i]
for i in range(3):
    row = np.zeros(9)
    row[i*3:(i+1)*3] = 1
    A_ub.append(row);  b_ub.append(supply[i])

# Demand constraints: sum_i x[i,j] ≥ demand[j]  →  −sum_i x[i,j] ≤ −demand[j]
for j in range(3):
    row = np.zeros(9)
    for i in range(3):
        row[i*3 + j] = -1
    A_ub.append(row);  b_ub.append(-demand[j])

# Soln
results = linprog(cost, A_ub=np.array(A_ub), b_ub=np.array(b_ub), bounds=[(0, None)]*9, method='highs')

# results
alloc = results.x.reshape(3, 3)
df = pd.DataFrame(alloc.astype(int), index=factories, columns=warehouses)

print("Optimal shipment plan (units):")
print(df.to_string())
print(f"\nMinimum total cost: {results.fun:.0f} BDT")


