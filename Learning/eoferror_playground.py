def main():

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