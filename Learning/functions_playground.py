"""
Topic:
    Functions

Purpose:
    Learn how functions organize reusable code.

Things to Learn:
    - Parameters
    - Return values
    - Default arguments
"""

def greet(name):
    print(f"Hello, {name}!")


def add(a, b):
    return a + b


def multiply(a, b = 1):
    return a * b


def main():

    greet("Evan")

    print(add(5, 7))

    print(multiply(10))

    print(multiply(10, 5))


if __name__ == "__main__":
    main()