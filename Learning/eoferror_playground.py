"""
Topic:
    EOFError

Purpose:
    Understand how EOFError occurs and how to gracefully handle end-of-file input.

Things to Learn:
    - What EOFError is
    - Catching EOFError
    - Infinite input loops
    - Breaking out of loops cleanly
    - EOF keyboard shortcuts (Ctrl+D on macOS/Linux, Ctrl+Z then Enter on Windows)
"""


def main():

    print("=== EOFError Handling ===")
    print("Instructions: \nWindows: Press Ctrl+Z + Enter to exit.\nMac/Linux: Press Ctrl+D to exit.\n")
    while True:
        try:
            name = input("Name: ")
            print(f"Hello {name}")
        except EOFError:
            print("\nEOF detected.")
            break


if __name__ == "__main__":
    main()