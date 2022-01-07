def main():
    name = input("What is your name (don't add spaces)? \n")
    name = name.lower()

    x = sum(int(ord(ch)) - 96 for ch in name)
    print("The numeric value of your name is {0}.".format(x))

main()

