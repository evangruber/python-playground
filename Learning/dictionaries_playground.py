"""
Topic:
    Dictionaries

Purpose:
    Learn how dictionaries store and retrieve key-value pairs.

Things to Learn:
    - Creating dictionaries
    - Accessing values
    - Adding and updating entries
    - Removing entries
    - Looping through dictionaries
"""

def main():

    student = {
        "name": "Evan",
        "age": 19,
        "grade": "A-"
    }

    print(student)
    print()

    print(student["name"])
    print(student.get("age"))
    print()

    student["grade"] = "A+"
    student["school"] = "Elementary"

    print(student)
    print()

    print("Keys:")
    for key in student:
        print(key)

    print()

    print("Items:")
    for key, value in student.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()