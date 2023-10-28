"""
calculate the value of integral of cos(x) dx from 0 to pi/4 using the simpson's 3/8 rule.
Divide the integration interval into N equally spaced points where N = 333.
"""

import math

def f(x):
    return math.cos(x)

def simpsons_3_8_rule(a, b, N):
    h = (b - a) / N  # Width of each subinterval
    integral = f(a) + f(b) 

    for i in range(1, N):
        x_i = a + i * h
        if i % 3 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 3 * f(x_i)

    integral *= 3 * h / 8
    return integral

a = 0
b = math.pi / 4
N = 333

result = simpsons_3_8_rule(a, b, N)
print(f"The approximate value of the integral is: {result}")
