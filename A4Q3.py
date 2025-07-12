#LPP_max

from scipy.optimize import linprog

# Coeffs of the objective function (negative for maximization; normally linprog minimizes)
c = [12, 15, 14]

# Inequality constraints matrix (Ax ≤ b)
A_ub = [
    [0.03, 0.02, 0.05],           # Ash constraint
    [0.0002, 0.0004, 0.0003]      # Phosphorous constraint
]
b_ub = [3, 0.03]                  # "ash not more than 3% and phosphorous not more than 0.03%" eta bolai chilo 

# Equality constraint: x1 + x2 + x3 = 100
A_eq = [[1, 1, 1]]
b_eq = [100]

# Bounds for x1, x2, x3 ≥ 0
bounds = [(0, None), (0, None), (0, None)]

# Soln
result = linprog(-c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# results
if result.success:
    print("Optimal solution found:")
    print(f"Coal A: {result.x[0]:.4f} tons")
    print(f"Coal B: {result.x[1]:.4f} tons")
    print(f"Coal C: {result.x[2]:.4f} tons")
    print(f"Maximum Profit: {-result.fun:.2f} BDT")
else:
    print("Optimization failed.")


