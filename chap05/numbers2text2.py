def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents. \n")

    #Get the message to encode
    instring = input("Please enter the Unicode-encoded message: ")

    #Loop through each substring and build Unicode message
    chars = []
    for num in instring.split():
        codenum = eval(num)
        chars.append(chr(codenum))          #accumulate new character

    message = "".join(chars)
    print("\nThe decoded message is:", message)

main()
