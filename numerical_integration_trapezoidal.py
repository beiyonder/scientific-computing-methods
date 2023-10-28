"""Calculate the approximate value of the integral x^2 dx from a to b 
using the trapezoidal rule. The numerical integration has to be performed over N points,
where N = 100 and a = 0 and b = 2. What will be the value of integral?
"""

def function(x):
    return x**6 - 5*x**5 + 3

def trapezoidal_rule(a, b, N):
    h = (b - a) / N
    integral = 0.5 * (function(a) + function(b))
    for i in range(1, N):
        integral += function(a + i * h)
    integral *= h
    return integral

a = 3
b = 5
N = 1000

result = trapezoidal_rule(a, b, N)
print("Approximate integral:", result)



#----------------For functions of two variables-----------
def f(x, y):
    return x**2 + y**2  # Define your 2-variable function here

def double_integral_trapezoidal(a, b, c, d, Nx, Ny):
    hx = (b - a) / Nx
    hy = (d - c) / Ny
    integral = 0.0

    for i in range(Nx):
        for j in range(Ny):
            xi = a + i * hx
            yj = c + j * hy

            term = f(xi, yj)

            # Corner points
            if i == 0 or i == Nx - 1:
                term *= 0.5
            if j == 0 or j == Ny - 1:
                term *= 0.5

            integral += term

    integral *= hx * hy
    return integral

a = 0
b = 2
c = 0
d = 3
Nx = 100
Ny = 100

# result = double_integral_trapezoidal(a, b, c, d, Nx, Ny)
# print(f"The approximate value of the double integral is: {result}")
