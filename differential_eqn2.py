# import numpy as np

# # Define the parameters
# delta_x = 0.01  # Step size
# final_x = 2.0  # Final value of x
# initial_condition = 1.0  # Initial condition

# # Initialize variables
# x = 0.0
# y = initial_condition

# # Perform the Euler Forward integration
# while x < final_x:
#     y_next = y + delta_x*(x + y + x * y)  # Update y using the differential equation
#     x += delta_x  # Update x
#     y = y_next  # Update y

# # The value of y at x=2.0
# y_at_2_0 = y

# # Print the result
# print(f"The value of y at x=2.0 is approximately {y_at_2_0:.4f}")




def euler_forward(differential_equation, x0, y0, x_target, deltax):
    x_values = [x0]
    y_values = [y0]

    while x_values[-1] < x_target:
        x_i = x_values[-1]
        y_i = y_values[-1]
        y_i_plus_1 = y_i + deltax * differential_equation(x_i, y_i)
        x_values.append(x_i + deltax)
        y_values.append(y_i_plus_1)

    return x_values, y_values

# Define the differential equation dy/dx = x + y + xy
def differential_equation(x, y):
    return x + y + x * y

x0 = 0
y0 = 1
x_target = 2
deltax = 0.01

x_values, y_values = euler_forward(differential_equation, x0, y0, x_target, deltax)

# Find the value of y when x = 2
x_target_index = x_values.index(x_target)
y_at_x_target = y_values[x_target_index]

print(f"y({x_target}) = {y_at_x_target}")
