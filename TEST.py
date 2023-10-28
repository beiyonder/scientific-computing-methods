import numpy as np
import matplotlib.pyplot as plt

# Parameters
D = 0.1  # Diffusion coefficient
L = 1.0  # Length of the domain
T = 1.0  # Total time
N = 100  # Number of grid points
M = 1000  # Number of time steps
dx = L / N  # Grid spacing
dt = T / M  # Time step size
r = D * dt / dx**2  # Stability parameter

# Initialize the grid
x = np.linspace(0, L, N+1)
u = np.sin(2 * np.pi * x)  # Initial condition

# Solve the diffusion equation
for i in range(M):
    # Apply periodic boundary conditions
    u[0] = u[N]
    u[N+1] = u[1]
    
    # Compute the next time step using the finite difference method
    u_new = u[1:N+1] + r * (u[2:N+2] - 2 * u[1:N+1] + u[0:N])
    
    # Update the grid
    u[1:N+1] = u_new

# Plot the final solution
plt.plot(x, u)
plt.xlabel('x')
plt.ylabel('u')
plt.title('Solution of the 1D Diffusion Equation')
plt.show()