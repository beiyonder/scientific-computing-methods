# # Define the differential equation as a function
# def f(t, x):
#     return (t - x) ** 2

# # Define the initial conditions
# t = 0.0
# x = 1.0
# delta_t = 0.01
# end_time = 1.0

# # Perform the RK2 integration
# while t < end_time:
#     # RK2 Step 1
#     k1 = delta_t * f(t, x)
#     # RK2 Step 2
#     k2 = delta_t * f(t + delta_t / 2, x + k1 / 2)
#     # Update x using the weighted average of k1 and k2
#     x = x + k2
    
#     # Update time
#     t += delta_t

# # The final value of x at t=1
# print(f"x(t=1) = {x}")


import numpy as np

def f(x, t):
    return (t - x) / 2

# Define the initial conditions
tinit = 0.0
tfinal = 1.0
dt = 0.01
initcond = 1.0

def runge_kutta(f, tinit, tfinal, dt, initcond):
    n = int((tfinal - tinit)/dt) + 1
    t = np.linspace(tinit, tfinal, n)
    x = np.zeros(n)
    x[0] = initcond

    for k in range(n - 1):
        xmid = x[k] + f(x[k], t[k])*dt/2
        x[k+1] = x[k] + f(xmid, t[k] + dt/2)*dt
    return t, x
# Call the runge_kutta function
t, x = runge_kutta(f, tinit, tfinal, dt, initcond)

# Print the final value of x at t=1
print(f"x(t=1) = {x[-1]}")