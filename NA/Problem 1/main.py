import math

f = lambda x: math.exp(x) - x**2

def bisection_method(a, b, tolerance):
    if (f(a) * f(b) >= 0):
        print("The given interval is incorrect, so no root can be found")
        return
    
    c = 0
    while ((b - a) >= tolerance):
        c = (a + b) / 2

        if (f(c) == 0):
            return c
        elif (f(c) * f(a) < 0):
            b = c
        else:
            a = c
    
    return c

print(f"The root of the given function f is: {bisection_method(-2, 0, 1e-8)}")