"""
Topic:
    Loops

Purpose:
    Explore Python looping techniques.

Things to Learn:
    - for loops
    - while loops
    - range()
    - break
    - continue
"""

def main():

    print("=== for loop ===")

    for number in range(5):
        print(number)

    print()

    print("=== while loop ===")

    counter = 0

    while counter < 5:
        print(counter)
        counter += 1

    print()

    print("=== break ===")

    for number in range(10):
        if number == 5:
            break

        print(number)

    print()

    print("=== continue ===")

    for number in range(10):
        if number % 2 == 0:
            continue

        print(number)


if __name__ == "__main__":
    main()