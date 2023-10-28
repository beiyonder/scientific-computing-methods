def f(x):
    return x**3 + 4*x**2 + 6*x + 8

def bisection(a, b, tol):
    while (b - a) / 2.0 > tol:
        mid = (a + b) / 2.0
        if f(mid) == 0:
            return round(mid, 2)
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return round((a + b) / 2.0, 2)

# Define the interval [a, b] and tolerance
a = -10.0
b = 10.0
tolerance = 1e-4

# Find the real root using the Bisection method
real_root = bisection(a, b, tolerance)

print("Real root of the equation:", real_root)
