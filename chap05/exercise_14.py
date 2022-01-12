#This program calculates avg word length, counts lines, total characters, and total words 
def main():
    fname = input("Enter filename: ")
    with open(fname, "r") as infile:
        data = infile.read()
        fileLines = infile.readlines()
        lines = list(fileLines)
        numWords = []
        letTotal = 0
        #loop for duration of input list split
        for string in data.split():
            x = string[0]
            numWords.append(x)
            letTotal = len(string) + letTotal
            wordAvg = letTotal / (len(numWords))
            
        print("There are {0} lines in the file.".format(len(lines)))
        print("The avg word length is: {0}".format(wordAvg))
        print("The total number of letters is: {0}".format(letTotal))
        print("The number of words is: {0}".format(len(numWords)))


main()
