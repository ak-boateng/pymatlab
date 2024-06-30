# Approximation of √2 using Newton-Raphson method

def newtonsmethod(func, deriv, x, n):
    # Use `exec` to create a function from the string representation of `func` and `deriv`
    # This avoids using eval inside the loop

    def f(x):
        return eval(func)

    def df(x):
        return eval(deriv)

    for intercept in range(1, n):
        # Update the current approximation using the Newton-Raphson formula
        x = x - (f(x) / df(x))
    
    # Print the result using proper string formatting
    print(f"The root was found to be {x} after {n} iterations")

# Test the newtonsmethod function with different starting points
newtonsmethod("x**2 - 2", "2*x", 2, 23)
newtonsmethod("x**2 - 2", "2*x", 4, 21)
