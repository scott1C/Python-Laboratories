from sympy import symbols, Matrix, sympify

def newton_raphson_method(equations, variables, init_guess, tolerance, max_iterations = 10000):
    F = Matrix(equations)
    J = F.jacobian(variables)
    x = Matrix(init_guess)

    for _ in range(max_iterations):
        F_value = F.subs(dict(zip(variables, x)))
        if (F_value.norm() < tolerance):
            return x
        J_value = J.subs(dict(zip(variables, x)))
        if (J_value.det() == 0):
            raise ValueError("The Jacobian matrix is not invertible! Try another guess!")
        delta_x = J_value.LUsolve(-F_value)
        x += delta_x
    else:
        print(f"The solution did not converge in {max_iterations} iterations")

num_equations = int(input("Enter the number of equations: "))
equations = []

for i in range(num_equations):
    eq_str = input(f"Enter the equation {i + 1}: ")
    equations.append(sympify(eq_str))

variables_str = input("Enter the variables separated by spaces: ")
variables = symbols(variables_str)

initial_guess_str = input("Enter the initial guesses separated by spaces: ")
initial_guess = [float(val) for val in initial_guess_str.split()]

tolerance = float(input("Enter the desired tolerance: "))

solution = newton_raphson_method(equations, variables, initial_guess, tolerance)
print(f"The roots are: {[root.evalf() for root in solution]}")