import numpy as np
from scipy.optimize import linear_sum_assignment

# Profit matrix (rows: salesmen A–D, columns: cities 1–4)
profit = np.array([
    [16, 10, 14, 11],
    [14, 11, 15, 15],
    [15, 15, 13, 12],
    [13, 12, 14, 15]
])

# converting cost matrix by taking negative
cost = -profit

# Hungarian algorithm
row_ind, col_ind = linear_sum_assignment(cost)

# assignments and total profit
total_profit = profit[row_ind, col_ind].sum()
assignments = list( zip("ABCD", (col_ind + 1)))  # City index +1 for 1-based indexing

print("Assignments:", assignments)
print("Total Profit:", total_profit)


