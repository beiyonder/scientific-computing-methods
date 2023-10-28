import numpy as np

# Define the function f(x, y)
def f(x, y):
    return 256 * (np.sin(x)**2) * (np.cos(2*y)**3)

# Define the grid size and limits
Nx, Ny = 64, 64
x = np.linspace(-np.pi, np.pi, Nx, endpoint=False)
y = np.linspace(-np.pi, np.pi, Ny, endpoint=False)
X, Y = np.meshgrid(x, y)

# Evaluate the function over the grid
f_values = f(X, Y)

# Compute the 2D Fourier Transform and normalize it
F_values = np.fft.fft2(f_values) / (Nx * Ny)

# Calculate the wave numbers associated with the Fourier amplitudes
kx = np.fft.fftfreq(Nx, d=(2 * np.pi) / Nx)
ky = np.fft.fftfreq(Ny, d=(2 * np.pi) / Ny)
KX, KY = np.meshgrid(kx, ky)

# Find the Fourier amplitude at (kx, ky) = (1.0, 1.0)
target_kx, target_ky = 1.0, 1.0

# Calculate the index closest to the target wave numbers
index_kx = np.argmin(np.abs(kx - target_kx))
index_ky = np.argmin(np.abs(ky - target_ky))

# Get the corresponding Fourier amplitude
fourier_amplitude = np.abs(F_values[index_ky, index_kx])

# Print the Fourier amplitude at (kx, ky) = (1.0, 1.0) rounded to four decimal places
print("Fourier amplitude at (kx, ky) = (1.0, 1.0): {:.4f}".format(fourier_amplitude))
