def main():

    example_input = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    print(f"example_input: {example_input}\n")

    print("Basic slicing")
    print("----------------")
    print(f"example_input[0:3]   -> {example_input[0:3]}")
    print(f"example_input[3:5]   -> {example_input[3:5]}")
    print(f"example_input[:5]    -> {example_input[:5]}")
    print(f"example_input[5:]    -> {example_input[5:]}")
    print()

    print("Negative indexes")
    print("----------------")
    print(f"example_input[-1:]   -> {example_input[-1:]}")
    print(f"example_input[-2:]   -> {example_input[-2:]}")
    print(f"example_input[-10:-5]-> {example_input[-10:-5]}")
    print()

    print("Step")
    print("----------------")
    print(f"example_input[::2]   -> {example_input[::2]}")
    print(f"example_input[::-1]  -> {example_input[::-1]}")

if __name__ == "__main__":
    main()