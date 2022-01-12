def counter():
    text = input("Input: \n")

    word_len = []
    #loop for duration of input list split
    for string in text.split():
        x = string[0]
        word_len.append(x)

    print(len(word_len))

counter()
