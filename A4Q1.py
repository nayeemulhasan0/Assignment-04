#LPP_graphical 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# constraints
def c1(x1): return (10 - x1)/2
def c2(x1): return 6 - x1
def c3(x1): return x1 - 2
def c4(x1): return (x1 - 1)/2

# plotting setup
plt.figure(figsize=(10, 8))
x = np.linspace(0, 6, 400)

# plotting constraint lines
plt.plot(x, c1(x), 'r-', label=r'$x_1 + 2x_2 \leq 10$')
plt.plot(x, c2(x), 'g-', label=r'$x_1 + x_2 \leq 6$')
plt.plot(x, c3(x), 'b-', label=r'$x_1 - x_2 \leq 2$')
plt.plot(x, c4(x), 'm-', label=r'$x_1 - 2x_2 \leq 1$')

# axes
plt.axvline(0, color='k', alpha=0.3)
plt.axhline(0, color='k', alpha=0.3)

# feasible region
vertices = [(0,0), (1,0), (3,1), (4,2), (2,4), (0,5)]
plt.gca().add_patch(Polygon(vertices, color='lightgray', alpha=0.5, label='Feasible Region'))

# objective function at max value
z_max = 10
plt.plot(x, z_max - 2*x, 'k--', label=r'$Z = 2x_1 + x_2 = 10$')

# labeling corner points
points = [(0,0), (1,0), (3,1), (4,2), (2,4), (0,5)]
for x1, x2 in points:
    z = 2*x1 + x2
    plt.plot(x1, x2, 'ro')
    plt.annotate(f'({x1},{x2})\nZ={z}', (x1, x2), xytext=(10,-10), 
                 textcoords='offset points', ha='center')

# optimal solution plot
plt.plot(4, 2, 'o', markersize=25, label='Optimal Solution (4,2)')

# showndorjo bordhon er kaj cholitese . . .
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title('Linear Programming Graphical Solution')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()

print("Optimal Solution: x1 = 4, x2 = 2")
print("Maximum Z = 2*4 + 2 = 10")


