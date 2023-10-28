import numpy as np

# Define the parameters
delta_t = 0.01  # Time step
final_time = 1.0  # Final time
initial_condition = 1.0  # Initial condition

# Initialize variables
t = 0.0
x = initial_condition

# Perform the Trapezoid method integration
while t < final_time:
    x_next = x + 0.5 * delta_t * (5 * x + 5 * (x + delta_t * 5 * x))  # Trapezoid rule
    t += delta_t
    x = x_next

# The value of x at t=1.0
x_at_1_0 = x

# Print the result
print(f"The value of x at t=1.0 is approximately {x_at_1_0:.4f}")
