"""solve the 1D diffusion equation with periodic boundary 
conditions using the finite difference method and RK2 time integration"""
import numpy as np

# Constants
L = 2 * np.pi        # Length of the domain
N = 64              # Number of grid points
T = 1.0             # Total simulation time
dt = 0.001          # Time step
h = L / N           # Grid spacing

# Create the grid
x = np.linspace(0, L, N, endpoint=False)  # Excluding the endpoint for periodic BC
dx = x[1] - x[0]

# Initial condition
def initial_condition(x):
    return np.exp(-2 * (x - np.pi)**2)

# Initialize the solution array
psi = initial_condition(x)

# Time integration using RK2
for t in np.arange(0, T, dt):
    # Save the current solution for the first stage
    psi_tmp = psi.copy()

    # Calculate the first stage of RK2
    d2psi = np.zeros(N)
    for i in range(N):
        d2psi[i] = (psi_tmp[(i + 1) % N] - 2 * psi_tmp[i] + psi_tmp[(i - 1) % N]) / dx**2

    k1 = dt * d2psi
    psi_tmp += 0.5 * k1

    # Calculate the second stage of RK2
    d2psi = np.zeros(N)
    for i in range(N):
        d2psi[i] = (psi_tmp[(i + 1) % N] - 2 * psi_tmp[i] + psi_tmp[(i - 1) % N]) / dx**2

    k2 = dt * d2psi

    # Update the solution using the weighted average of k1 and k2
    psi += 0.5 * (k1 + k2)

# Find the maximum value of ϕ(x, t=1)
max_value = np.max(psi)

# Print the result rounded to 4 decimal places
print(f"Maximum value of ϕ(x, t=1): {max_value:.4f}")
