import math


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a, b):
        return a ** b

    @staticmethod
    def square_root(a):
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(a)

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if not isinstance(n, int):
            raise TypeError("Factorial is only defined for integers")
        return math.factorial(n)

    @staticmethod
    def sin(x):
        return math.sin(x)

    @staticmethod
    def cos(x):
        return math.cos(x)

    @staticmethod
    def tan(x):
        return math.tan(x)

    @staticmethod
    def log(x, base=math.e):
        if x <= 0:
            raise ValueError("Logarithm is only defined for positive numbers")
        if base <= 0 or base == 1:
            raise ValueError("Base must be positive and not equal to 1")
        return math.log(x, base)

    @staticmethod
    def exp(x):
        return math.exp(x)