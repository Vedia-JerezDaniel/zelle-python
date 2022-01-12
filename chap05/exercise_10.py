#word count
def counter10():
    text = input("Input: \n")
    numWords = []
    #loop for duration of input list split
    for string in text.split():
        x = string[0]
        numWords.append(x)

    letTotal = 0
    for string in text.split():
        letTotal = len(string) + letTotal
        wordAvg = letTotal / (len(numWords))
    print(letTotal)    
    print("The word average is: ", wordAvg)

counter10()
