import numpy as np

Cost = np.array([
    [4, 3, 1, 2, 6],
    [5, 2, 3, 4, 5],
    [3, 5, 6, 3, 2],
    [2, 4, 4, 5, 3]
])
Supply = np.array([80, 60, 40, 20])
Demand = np.array([60, 60, 30, 40, 10])

def northwest(Supply, Demand):
    s, d = Supply.copy(), Demand.copy()
    X = np.zeros_like(Cost)
    i = j = 0
    while i < len(s) and j < len(d):
        q = min(s[i], d[j])
        X[i, j] = q
        s[i] -= q; d[j] -= q
        if s[i] == 0: i += 1
        if d[j] == 0: j += 1
    return X

def least_cost(Supply, Demand, Cost):
    s, d = Supply.copy(), Demand.copy()
    X = np.zeros_like(Cost)
    while s.sum() and d.sum():
        mask = (s[:, None] > 0) & (d > 0)
        i, j = np.unravel_index(np.argmin(np.where(mask, Cost, np.inf)), Cost.shape)
        q = min(s[i], d[j])
        X[i, j] = q
        s[i] -= q; d[j] -= q
    return X

for name, fn in [('NW-Corner', northwest), ('Least-Cost', least_cost)]:
    X = fn(Supply, Demand, Cost) if fn is least_cost else fn(Supply, Demand)
    total = (X * Cost).sum()
    print(f"{name}: cost = {total}")
    print(X, "\n")

