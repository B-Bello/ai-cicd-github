"""Simple utility functions - you'll add more!"""


def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]

def multiply(a: int, b: int):
    """Mutltiply two numbers"""
    return a * b

def factorial(n):
    if n < 0:
        print("Error, factorial not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)