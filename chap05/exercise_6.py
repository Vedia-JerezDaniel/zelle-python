def main():
    #Get name from user and store as a string
    name = input("What is your name? \n")

    #Convert to all lower, and account for user input
    fullName = "".join(name)
    fullName = fullName.lower()
    fullName = fullName.lstrip()
    fullName = fullName.replace(" ", "")
    fullName = fullName.replace("-", "")

    #Convert to numbers, subtract 96 from each, and accumulate
    print(fullName)
    x = sum(int(ord(ch)) - 96 for ch in fullName)

    print("The numeric value of your name is {0}.".format(x))

main()
