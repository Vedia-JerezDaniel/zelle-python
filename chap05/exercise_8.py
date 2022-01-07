def main():
    p_text = input("Enter the message you'd like encrypted.\n")
    p_text = p_text.replace(" ", "_")
    p_text = p_text.lower()
 
    key = eval(input("What's the key? : "))
    table = "abcdefghijklmnopqrstuvwxyz"

    c_text = "".join(table[((ord(ch)) - 97) + (key % 52)] for ch in p_text)
    print("Your encoded message is {0}.".format(c_text))

main()
ord('_')

