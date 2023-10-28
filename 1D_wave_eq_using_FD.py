"""Solve the 1D wave equation numerically using 
Finite difference method with periodic boundary conditions. 
The wave equation is written as:
                    
                ∂Ψ/∂t=-1.5∂Ψ/∂x

Solve the PDE in  box  [0,2π]
by using N = 512 grid points. Choose the correct values  of (Ψ)
 (round answer upto two decimal place) at t=1 and x=3.48 (to get x=3.48 round 
 the x array upto two decimal place) from the options given below.


Note:
• Use periodic boundary condition
• Use the following function as initial condition: Ψ(x,0)=e^(-32(x-2)^2)

• Use RK-2 method for performing the time integration and two point central scheme for evaluating the derivative on the RHS. Discretize the domain with an appropriate grid spacing h

• Choose N = 500 and  Δt=0.001"""

import numpy as np

# Constants
L = 2 * np.pi        # Length of the domain
N = 512             # Number of grid points
T = 1.0             # Total simulation time
dt = 0.001          # Time step
h = L / N           # Grid spacing
x_value = 3.48      # The x value at which we want to find Ψ

# Create the grid
x = np.linspace(0, L, N, endpoint=False)  # Excluding the endpoint for periodic BC
dx = x[1] - x[0]

# Initial condition
def initial_condition(x):
    return np.exp(-32 * (x - 2)**2)

# Initialize the solution arrays
psi = initial_condition(x)

# Time integration using RK2
for t in np.arange(0, T, dt):
    psi_new = np.zeros(N)
    
    # Calculate the first stage of RK2
    for i in range(N):
        dpsi = -1.5 * (psi[(i + 1) % N] - psi[(i - 1) % N]) / (2 * dx)
        psi_new[i] = psi[i] + 0.5 * dt * dpsi

    # Calculate the second stage of RK2
    for i in range(N):
        dpsi = -1.5 * (psi_new[(i + 1) % N] - psi_new[(i - 1) % N]) / (2 * dx)
        psi[i] = psi[i] + dt * dpsi

# Find the value of Ψ at x=3.48 (rounded to two decimal places) at t=1
x_target = 3.48
index = int(round(x_target / L * N))  # Taking periodic boundary conditions into account
psi_at_x_target = psi[index]

# Print the result
print(f"Ψ at x={x_target:.2f} and t=1: {psi_at_x_target:.2f}")
