# Write a program that solves word jumble problems. 

# Program generates all anagrams of an array, then checks them against 
# a dictionary. The program prints the dictionary word(s) > 4 letters that correspond(s) 
# with the anagram. 

class WordTruer:
    def __init__(self, dictionary, string):
        self.dictionary = dictionary
        self.string = string
        self.anagrams = self.permute(self.string)
        self.twords = []
        self.dwords = []
        self.read_dict()
        self.check_anagrams()
        self.summary()

    def read_dict(self):
        with open(self.dictionary, 'r') as f:
            for word in f.readlines():
                self.dwords.append(word.strip())

    def permute(self, s):
        p = []
        if len(s) <= 1:
            p = [s]
        else:
            for i, l in enumerate(s):
                for p in self.permute(s[:i] + s[i+1:]):
                    p += [l + p] 
        return p
    
    def check_anagrams(self):
        for a in self.anagrams:
            if self.binary_search(self.dwords, a):
                self.twords.append(a)

    def binary_search(self, arr, inword):
        if len(arr) == 0:
            return False
        mid = len(arr) // 2
        dictword = arr[mid]
        if inword == dictword:
            return True
        left = arr[:mid]
        right = arr[mid+1:]

        if inword < dictword:
            return self.binary_search(left, inword)
        else:
            return self.binary_search(right, inword)

    def summary(self):
        for word in self.twords:
            print(word)


WordTruer('eng_dictionary.txt', 'fish')