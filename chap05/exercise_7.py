p_text = input("Enter the message you'd like encrypted.\n")

def main():

    key = eval(input("What's the key? : "))

    c_text = "".join((chr(ord(ch) + key)) for ch in p_text)
    print("Your encoded message is {0}.".format(c_text))

main()

def decrypt():
    d_text = input("Enter the encrypted message.\n")
    key = eval(input("What's the key? : "))*-1

    c_text = "".join((chr(ord(ch) + key)) for ch in d_text)
    c_text = c_text.replace("_", " ")
    print("Your encoded message is {0}.".format(c_text))
    
decrypt()