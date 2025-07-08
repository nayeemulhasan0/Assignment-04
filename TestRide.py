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

# Build A_ub and b_ub for supply ≤ and demand ≥ constraints
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

# Solve
res = linprog(cost,
              A_ub=np.array(A_ub), b_ub=np.array(b_ub),
              bounds=[(0, None)]*9,
              method='highs')

# Format result
alloc = res.x.reshape(3, 3)
df = pd.DataFrame(alloc.astype(int), index=factories, columns=warehouses)

print("Optimal shipment plan (units):")
print(df.to_string())
print(f"\nMinimum total cost: {res.fun:.0f} BDT")






















# from pulp import *

# # Define supply, demand, and costs
# supply = {'F1': 200, 'F2': 160, 'F3': 90}
# demand = {'W1': 180, 'W2': 120, 'W3': 150}
# costs = {
#     'F1': {'W1': 16, 'W2': 20, 'W3': 12},
#     'F2': {'W1': 14, 'W2': 8, 'W3': 18},
#     'F3': {'W1': 26, 'W2': 24, 'W3': 16}
# }

# # Create the linear programming problem
# prob = LpProblem("Transportation_Problem", LpMinimize)

# # Define decision variables
# vars = LpVariable.dicts("Route", (supply.keys(), demand.keys()), 0, None, LpContinuous)

# # Set the objective function (minimize total cost)
# prob += lpSum([vars[f][w] * costs[f][w] for f in supply for w in demand]), "Total Cost"

# # Add supply constraints
# for f in supply:
#     prob += lpSum([vars[f][w] for w in demand]) == supply[f], f"Supply_{f}"

# # Add demand constraints
# for w in demand:
#     prob += lpSum([vars[f][w] for f in supply]) == demand[w], f"Demand_{w}"

# # Solve the problem
# prob.solve()

# # Print the results
# print("Status:", LpStatus[prob.status])
# print("\nOptimal Shipping Plan:")
# for v in prob.variables():
#     if v.varValue > 0:
#         print(f"{v.name.replace('_', ' to ')}: {v.varValue} units")
# print(f"\nTotal Shipping Cost: {value(prob.objective)} BDT")








