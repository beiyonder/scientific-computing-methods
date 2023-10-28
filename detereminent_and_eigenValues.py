import numpy as np
from scipy import linalg

# Define the matrix A
A = np.array([[1, 2, 3], [2, 1, 4], [3, 4, 2]])

B = np.array([[1, 0], [0, -1]])

C = np.array([[2, 0, 0], [0, 2, 3], [0, -3, 2]])
# Calculate the determinant of A
determinant = round(linalg.det(C), 2)

# Calculate the eigenvalues of A
eigenvalues, _ = linalg.eig(C)

# Find the maximum eigenvalue (discard the imaginary part)
# max_eigenvalue = round(max(eigenvalues.real), 2)
sum_eigenValues  = sum(eigenvalues.real)
prod_eigenValues = round(np.prod(eigenvalues), 2)

print(sum_eigenValues, prod_eigenValues)
# print("Determinant of B:", determinant)
# # print("Maximum Eigenvalue of A:", max_eigenvalue)
# for val in eigenvalues:
#     print(val, end=" ")
