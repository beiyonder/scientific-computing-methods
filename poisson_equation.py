import numpy as np

# Constants
n = 64  # Grid size
tolerance = 1e-6  # Tolerance for convergence
max_iterations = 10000  # Maximum number of iterations
L = 2.0  # Box size

# Calculate the grid spacing
dx = L / (n + 1)

# Initialize the grid
phi = np.zeros((n, n), dtype=float)

# Jacobi method iteration
iteration = 0
delta_phi = tolerance + 1  # Initial value for delta_phi

# Define the source term function based on grid coordinates
def source_term(i, j):
    x = -1 + (i + 1) * dx
    y = -1 + (j + 1) * dx
    r_sq = x**2 + y**2
    return np.exp(-24 * r_sq)

# Jacobi method iteration
while delta_phi > tolerance and iteration < max_iterations:
    delta_phi = 0
    new_phi = np.copy(phi)
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            new_phi[i, j] = 0.25 * (phi[i + 1, j] + phi[i - 1, j] + phi[i, j + 1] + phi[i, j - 1] - dx**2 * source_term(i, j))
            delta_phi = max(delta_phi, abs(new_phi[i, j] - phi[i, j]))
    phi = new_phi
    iteration += 1

# Find the value of phi at the specified point
value_at_point = phi[61, 61]

# Round the result to four decimal places
rounded_value = round(value_at_point, 4)

# Output the result
print(f"Value of phi at the specified point: {rounded_value}")
print(f"Iterations required for convergence: {iteration}")
