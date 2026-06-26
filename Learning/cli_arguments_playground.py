"""
Topic:
    Command-Line Arguments

Purpose:
    Learn how Python receives arguments from the terminal.

Things to Learn:
    - sys.argv
    - Argument length
    - Accessing arguments
"""

import sys


def main():

    print(sys.argv)
    print()

    print(f"Number of arguments: {len(sys.argv)}")
    print()

    if len(sys.argv) > 1:
        print("=== Arguments ===")

        for argument in sys.argv[1:]:
            print(argument)
    else:
        print("No arguments provided.")


if __name__ == "__main__":
    main()