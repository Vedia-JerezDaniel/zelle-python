#censorship program

def main():
    filename = 'chap11/exercise_11.txt'
    infile = open(filename, 'r')
    with open('chap11/exercise_11(1).txt', 'w') as outfile:
        for line in infile:
            words = line.split()
            for i in range(len(words)):
                if len(words[i]) == 4:
                    words[i] = '****'
            line = ' '.join(words)
            print((line), file = outfile)
        infile.close()

main()

