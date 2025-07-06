#math functions using numpy
import numpy as np
def add(a, b):
    """Returns the sum of a and b."""
    return np.add(a, b) 
def subtract(a, b):
    """Returns the difference of a and b."""
    return np.subtract(a, b)
def multiply(a, b):
    """Returns the product of a and b."""
    return np.multiply(a, b)
def divide(a, b):
    """Returns the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return np.divide(a, b)
def power(a, b):
    """Returns a raised to the power of b."""
    return np.power(a, b)
def square_root(a):
    """Returns the square root of a."""
    if a < 0:
        raise ValueError("Cannot compute square root of negative number.")
    return np.sqrt(a)
def absolute_value(a):
    """Returns the absolute value of a."""
    return np.abs(a)
def factorial(n):
    """Returns the factorial of n."""
    if n < 0:
        raise ValueError("Cannot compute factorial of negative number.")
    return np.math.factorial(n)
def logarithm(a, base=np.e):
    """Returns the logarithm of a to the given base."""
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers.")
    return np.log(a) / np.log(base)
print("Math functions loaded successfully.")
# Example usage:
if __name__ == "__main__":
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    print("Multiplication:", multiply(5, 3))
    print("Division:", divide(5, 3))
    print("Power:", power(5, 3))
    print("Square Root:", square_root(25))
    print("Absolute Value:", absolute_value(-5))
    print("Factorial:", factorial(5))
    print("Logarithm:", logarithm(100, 10)) 