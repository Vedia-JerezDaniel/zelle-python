def acronym(phrase):
    words = []
    for st in phrase.split():
        x = st[0].upper()
        words.append(x)
    return "".join(words)

def main():
    phrase = input("What would you like acronymized? \n")
    print(acronym(phrase))

main()
