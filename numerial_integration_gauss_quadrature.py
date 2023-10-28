import math

def f(x, a):
    return 1 + a * (x**2)

def gauss_quadrature_two_point(a):
    weights = [1, 1]
    nodes = [-1 / 3**0.5, 1 / 3**0.5]

    integral = 0

    for i in range(2):
        integral += weights[i] * f(nodes[i], a)

    return integral

a = 2

result = gauss_quadrature_two_point(a)
print(f"The approximate value of the integral for a = 2 is: {result}")



#---------------Three-point Hermite-Gauss quadrature rule----------

def f(x, a):
    return math.exp(-x**2) * (a * x**2)

def hermite_gauss_quadrature_three_point(a):
    weights = [1.18164, 0.295409, 0.295409]
    nodes = [0, -1.22474, 1.22474]

    integral = 0

    for i in range(3):
        integral += weights[i] * f(nodes[i], a)

    return integral

a = 2

result = hermite_gauss_quadrature_three_point(a)
print(f"The approximate value of the integral for a = 2 is: {result}")
