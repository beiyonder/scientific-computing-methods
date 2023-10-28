import numpy as np
"""
Solving the differential eqn dx/dt = x + e^t, 
using predictor-corrector scheme. 
"""
# Define the differential equation as a function
def f(t, x):
    return x + np.exp(t)

# Define the initial conditions
tinit = 0.0
tfinal = 2.0
dt = 0.01
initcond = 1.0

# Implement the Predictor-Corrector integration method
def predictor_corrector(f, tinit, tfinal, dt, initcond):
    n = int((tfinal - tinit) / dt) + 1
    t = np.linspace(tinit, tfinal, n)
    x = np.zeros(n)
    x[0] = initcond

    for i in range(1, n):
        # Predictor step (using Euler's method)
        x_predictor = x[i - 1] + dt * f(t[i - 1], x[i - 1])
        
        # Corrector step (using the corrected slope)
        x_corrector = x[i - 1] + 0.5 * dt * (f(t[i - 1], x[i - 1]) + f(t[i], x_predictor))
        
        x[i] = x_corrector

    return t, x

# Call the predictor_corrector function
t, x = predictor_corrector(f, tinit, tfinal, dt, initcond)

# Print the value of x at t=2
print(f"x(t=2) = {x[-1]}")
