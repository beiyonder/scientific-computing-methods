import numpy as np
from scipy.fft import fft
from scipy.integrate import quad

"""
Calculate the integral ∫e^-(2*x^4)dx from -L to L
 numerically using Parseval's Theorem. Take L = 4π
 and the grid size to be 256.
"""
# Define the function to be integrated
def f(x):
    return np.exp(-2 * x**4)

# Define the integration limits and grid size
L = 4 * np.pi
N = 256

# Discretize the grid
dx = 2 * L / (N - 1)
x = np.linspace(-L, L, N)

# Calculate the function values
f_values = f(x)

# Perform the discrete Fourier transform (DFT)
F_values = fft(f_values)

# Calculate the frequency values manually
k = 2 * np.pi * np.fft.fftfreq(N, dx)

# Calculate the integral in x-space
integral_x_space = np.sum(f_values) * dx

# Calculate the integral in k-space
integral_k_space = np.sum(np.abs(F_values)**2) * dx

# Calculate the integral using SciPy's quad function as a reference
reference_integral, _ = quad(f, -L, L)

# Print the results
print("Numerical Integral in x-space:", integral_x_space)
print("Numerical Integral in k-space:", integral_k_space)
print("Reference Integral:", reference_integral)
