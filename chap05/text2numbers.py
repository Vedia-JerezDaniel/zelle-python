def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message.")

    message = input("Please enter the message to encode: ")

    print("\nHere are the Unicode codes:")

    for i in message:
        print(ord(i), end=" ")

    print()

main()
