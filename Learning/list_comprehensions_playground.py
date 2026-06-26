"""
Topic:
    List Comprehensions

Purpose:
    Learn how to create lists concisely.

Things to Learn:
    - Basic syntax
    - Conditions
    - Expressions
"""

def main():

    numbers = [1, 2, 3, 4, 5]

    print("Original:")
    print(numbers)
    print()

    print("Squares:")

    squares = [number ** 2 for number in numbers]

    print(squares)
    print()

    print("Even numbers:")

    evens = [number for number in numbers if number % 2 == 0]

    print(evens)
    print()

    print("Uppercase:")

    words = ["python", "playground", "learning"]

    uppercase = [word.upper() for word in words]

    print(uppercase)


if __name__ == "__main__":
    main()