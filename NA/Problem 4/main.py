from sympy import symbols, sympify

def hybrid_method(f, x0, x1, tol=1e-8, max_iter=10000):
    x = symbols('x')
    if f.subs(x, x0) * f.subs(x, x1) > 0:
        print("You have entered an incorrect range")
        return None
    for _ in range(max_iter):
        # Secant method
        x2 = x1 - f.subs(x, x1)*(x1-x0) / (f.subs(x, x1) - f.subs(x, x0))
        if x0 < x2 < x1 and abs(f.subs(x, x2)) < abs(f.subs(x, x1)):
            x0, x1 = x1, x2
        else:
            # Bisection method
            x2 = (x0 + x1) / 2
            if f.subs(x, x2) == 0:
                return x2
            elif f.subs(x, x2) * f.subs(x, x0) < 0:
                x1 = x2
            else:
                x0 = x2
        if abs(x1 - x0) < tol or abs(f.subs(x, x1)) < tol:
            return x1
        
    print("The method did not converge")
    return None

eq_str = input("Enter your equation: ")
range_str = input("Enter the range separated by space: ")
range_ = [float(point) for point in range_str.split()]
a, b = range_

eq = sympify(eq_str)
print(a, b)
root = hybrid_method(eq, a, b)
print("Root found:", root.evalf())
