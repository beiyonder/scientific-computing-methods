def polynomial_function(x):
    # return x + x**4 + x**6
    # return x + (x**2)/2 + (x**3)/3
    return x**2 + 4*x

def first_derivative_twoPoint_forward(f, x, h):
    derivative = (f(x+h) - f(x))/h
    return derivative
def first_derivative_threePoint_central(f, x, h):
    derivative = (f(x+h) - f(x-h))/(2*h)
    return derivative
"""
two-point forward difference scheme: f'(x) ≈ (f(x+h) - f(h))/h
three-point central difference scheme: f'(x) ≈ (f(x+h) - f(x-h))/2h

two-points backward difference sheme : f'(x) ≈ (f(x) - f(x - h))/h
"""
x_value = 1
step_size= 0.01 # h

# result = first_derivative(polynomial_function, x_value, step_size)
result = first_derivative_threePoint_central(polynomial_function, x_value, step_size)
print(result)
