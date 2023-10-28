import numpy as np
from scipy import linalg

# Coefficient matrix
A = np.array([[3, 4, -1], [1, 2, 1], [5, -1, 7]])

# Right-hand side vector
B = np.array([2, 11, 15])

# Solve the system of equations
solution = linalg.solve(A, B)

# Calculate the sum of x, y, and z
sum_xyz = round(np.sum(solution), 2)

print("Sum of (x + y + z):", sum_xyz)
