import numpy as np

"""
Differential Equation: d^2y/dt^2 + 2*(dy/dt) + 5y = 0 
"""

# Define the parameters
delta_t = 0.01  # Time step
final_time = 1.5  # Final time
initial_y = 2.0  # Initial value of y
initial_z = -4.0  # Initial value of dy/dt

# Initialize variables
t = 0.0
y = initial_y
z = initial_z

# Perform the Euler forward integration
while t < final_time:
    y_next = y + z * delta_t
    z_next = z - 2 * z * delta_t - 5 * y * delta_t
    t += delta_t
    y = y_next
    z = z_next

# The value of y at t=1.5
y_at_1_5 = y

# Print the result
print(f"The value of y at t=1.5 is approximately {y_at_1_5:.4f}")
