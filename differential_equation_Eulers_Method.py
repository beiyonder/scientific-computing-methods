import numpy as np

# Define the parameters
delta_t = 0.01  # Time step
final_time = 2 # Final time
initial_condition = 0  # Initial condition

# Define the differential equation function
def differential_equation(x):
    # dxdt = -2 * x  # The differential equation dx/dt + 2x = 0
    # dxdt = x + x*t
    # dxdt = x**2 - 0.1*x
    dxdt = -0.4*x + 4.8
    return dxdt



def backward():
    # Perform the Euler backward integration
    t = 0.0
    x = initial_condition
    while t < final_time:
        x_next = x / (1 + 2 * delta_t)
        x_next = x/(1 - (x*t + x)*delta_t)
        x_next = x / (1 - (x**2 - 0.1*x)*delta_t)
        x_next = x + differential_equation(x) * delta_t
        t += delta_t
        x = x_next
    return x

def forward():
    #Perform the Euler forward integration
    t = 0
    x = initial_condition
    while t< final_time:
        x_next = x  + differential_equation(x)* delta_t
        t += delta_t
        x = x_next
    return x


