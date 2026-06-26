"""
Topic:
    Exception Handling

Purpose:
    Learn how Python handles runtime errors using try/except blocks.

Things to Learn:
    - try and except
    - Catching specific exceptions
    - Using the exception object (as e)
    - else and finally blocks
    - Common built-in exceptions
"""


def main():

    print("=== ZeroDivisionError ===")

    try:
        print(divide(10, 0))
    except ZeroDivisionError as e:
        print(e)

    print()

    print("=== ValueError ===")

    try:
        number = int("hello")
    except ValueError as e:
        print(e)

    print()

    print("=== IndexError ===")

    try:
        numbers = [1, 2, 3]
        print(numbers[5])
    except IndexError as e:
        print(e)


def divide(a, b):
    return a / b

'''
Add later:
FileNotFoundError
TypeError
KeyError
NameError
AttributeError
'''

if __name__ == "__main__":
    main()