from sympy import symbols, Eq, solve

f = lambda x: x**3 + 2*x**2 + 10*x - 20
x = symbols('x')
def muller_method(x1, x2, x3, tolerance):
    while (abs(f(x3)) >= tolerance):
        lagrange_polynomial = f(x1)*((x-x2)/(x1-x2)*(x-x3)/(x1-x3)) + f(x2)*((x-x1)/(x2-x1)*(x-x3)/(x2-x3)) + f(x3)*((x-x1)/(x3-x1)*(x-x2)/(x3-x2))
        roots = solve(Eq(lagrange_polynomial, 0), x)
        x1 = x2
        x2 = x3
        if (abs(f(roots[0]).evalf()) <= abs(f(roots[1]).evalf())):
            x3 = roots[0].evalf()
        else:
            x3 = roots[1].evalf()

        return x3

print(f"The root for our function f is: {muller_method(0, 1, 2, 1e-8)}")
