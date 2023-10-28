
#--------------Doesn't work----------------------



import numpy as np

# Define constants
N = 128
V0 = 4
epsilon = 1e-6

# Initialize grid
phi = np.zeros((N, N))
phi[:, 0] = V0

# Iterate until convergence
while True:
    phi_new = np.zeros((N, N))
    for i in range(1, N-1):
        for j in range(1, N-1):
            phi_new[i, j] = (phi[i+1, j] + phi[i-1, j] + phi[i, j+1] + phi[i, j-1]) / 4
    if np.max(np.abs(phi_new - phi)) < epsilon:
        break
    phi = phi_new

# Find value of phi at (3, N-4)
phi_3_N_4 = phi[2, -4]

# Round off answer to two decimal places
phi_3_N_4_rounded = phi_3_N_4

print(f"The value of ϕ at (3, {N-4}) is {phi_3_N_4_rounded}")



