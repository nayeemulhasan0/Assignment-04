import numpy as np
from scipy.optimize import linear_sum_assignment

profit = np.array([
    [16, 10, 14, 11],
    [14, 11, 15, 15],
    [15, 15, 13, 12],
    [13, 12, 14, 15]
])

cost= - profit

x,y = linear_sum_assignment(cost)

assignment=list(zip("ABCD", (y + 1)))

print(f"assignment: {assignment}")
print(f"profit: {profit[x, y].sum()}")
