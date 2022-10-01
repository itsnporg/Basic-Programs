# Newton Raphson Method

import sympy
from sympy import *

x_symb = symbols('x')

# Taking equation as string
function = input("Enter the function: ")
iter = int(input("Enter number of iterations: "))
x_value = float(input("Enter the value of x: "))
decimal_points = int(input("Enter number after decimal points: "))

# Finding Derivative function
der_fx = Derivative(function, x_symb).doit()


# Converting Strings to SymPy Expressions
fx0_sympy = sympify(function)

print(f"Expression : \n{function}")
print(f"\nValue of the derivative : \n{der_fx} ")
for i in range(iter):
    # Final Calculations
    fx0 = round(fx0_sympy.subs(x_symb, x_value), decimal_points)
    der_fx0 = round(der_fx.subs(x_symb, x_value), decimal_points)
    x1 = round(x_value - (fx0)/der_fx0, decimal_points)

    print(f"Value of f({x_value}): {fx0:.{decimal_points}f}")
    print(f"Value of f'({x_value}): {der_fx0:.{decimal_points}f}")
    print(f"Value of x({i+1}): {x1:.{decimal_points}f}\n")
    x_value = x1