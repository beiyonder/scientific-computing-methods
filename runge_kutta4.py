import numpy as np
"""
Solving differential equation: dx/dt = -xcos(t)
Using RK4 (4th order Runge-kutta scheme)

initial conditions and steps are specified below.
"""
# Define the differential equation as a function
def f(t, x):
    return -x * np.cos(t)

# Define the initial conditions
tinit = 0.0
tfinal = 1.0
dt = 0.01
initcond = 1/2

# Implement the RK4 integration method
def runge_kutta4(f, tinit, tfinal, dt, initcond):
    n = int((tfinal - tinit) / dt) + 1
    t = np.linspace(tinit, tfinal, n)
    x = np.zeros(n)
    x[0] = initcond

    for i in range(1, n):
        k1 = dt * f(t[i - 1], x[i - 1])
        k2 = dt * f(t[i - 1] + 0.5 * dt, x[i - 1] + 0.5 * k1)
        k3 = dt * f(t[i - 1] + 0.5 * dt, x[i - 1] + 0.5 * k2)
        k4 = dt * f(t[i - 1] + dt, x[i - 1] + k3)

        x[i] = x[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t, x

# Call the runge_kutta4 function
t, x = runge_kutta4(f, tinit, tfinal, dt, initcond)

# Print the value of x at t=1
print(f"x(t=1) = {x[-1]}")
