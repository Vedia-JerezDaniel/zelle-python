#censorship program
def illegalWord(word):
    filename = 'chap11/exercise_12.txt'
    text = open(filename, 'r')
    censors = text.readlines()
    for i in range(len(censors)):
         censors[i] = censors[i].strip('\n')
    for cen in censors:
        if word == cen:
            return True
        
def main():
    filename = 'chap11/exercise_11.txt'
    infile = open(filename, 'r')
    with open('chap11/exercise_11(1).txt', 'w') as outfile:
        for line in infile:
            words = line.split()
            for i in range(len(words)):
                if illegalWord(words[i]):
                    words[i] = '*'
            line = ' '.join(words)
            print((line), file = outfile)
        infile.close()

main()

