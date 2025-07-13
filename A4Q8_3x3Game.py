import nashpy as nash
import numpy as np

B = np.array([[-1, -2, 8], [7, 5, -1], [6, 0, 12]])
A= np.transpose(B)
game = nash.Game(A, -A)

for a, b in game.vertex_enumeration():
    print(a.round(4), b.round(4), game[a, b].round(4)) 
