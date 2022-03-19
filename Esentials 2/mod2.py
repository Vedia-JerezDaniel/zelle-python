import math

math.sin()

sin()

from random import randint

for i in range(2):
    print(randint(1,2), end='')

import math
res = math.e != math.pow(2,4)
print(int(res))

import sin from math
from math import sin


the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
    
    
# LAB 1

def my_split(s, delim):
    for i, c in enumerate(s):
        if c == delim:
            return [s[:i]] + my_split(s[i + 1 :], delim)
    return [s]

a = "To be or not to be, that is the question"

my_split(a,' ')

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])


strNumbers = [zero, one, two, three, four, five, six, seven, eight, nine]
checkNumbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

check = False
while not check:
    userInput = input("Enter numbers: ")
    check = all(item in checkNumbers for item in userInput)
    
strList = []
for i in userInput:
    if i == '0':
        strList.append(strNumbers[0].strip('\n').split('\n'))
    elif i == '1':
        strList.append(strNumbers[1].strip('\n').split('\n'))
    elif i == '2':
        strList.append(strNumbers[2].strip('\n').split('\n'))
    elif i == '3':
        strList.append(strNumbers[3].strip('\n').split('\n'))
    elif i == '4':
        strList.append(strNumbers[4].strip('\n').split('\n'))
    elif i == '5':
        strList.append(strNumbers[5].strip('\n').split('\n'))
    elif i == '6':
        strList.append(strNumbers[6].strip('\n').split('\n'))
    elif i == '7':
        strList.append(strNumbers[7].strip('\n').split('\n'))
    elif i == '8':
        strList.append(strNumbers[8].strip('\n').split('\n'))
    elif i == '9':
        strList.append(strNumbers[9].strip('\n').split('\n'))

newStr = ''
for i in range(5):
    for item_ in strList:
        newStr += f'{item_[i]} '
    newStr += '\n'

print(newStr)


# Caesar cipher.
text = input("Enter your message: ")
skip = int(input("Skip number: "))

cipher = ''
for char in text:
    # if not char.isalpha():
    #     continue
    char = char.upper()
    code = ord(char) + skip
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)


# Caesar cipher - decrypting a message. al reves
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)


# Numbers Processor.

line = input("Enter a line of numbers - separate them with spaces: ")

strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")

# IBAN Validator.
# FR76 30003 03620 00020216907 50
iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')
type(iban)

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
            # es decir A = 10 ->x -> (10 + ord('A') - ord('A'))
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")

# LAB 2 PALINDROME

string=input(("Enter a string:"))
string.lower()
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")
      
# LAB 3 ANAGRAM

def check(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    print(s2)
    # the sorted strings are checked
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
# driver code 
s1 ="listen "
s2 ="silenT "
check(s1, s2)


# LAB 4 DIGIT OF LIFE

def digitoflife(date):
    if len(date) > 8:
        print("date inputed is long and bad")
    else:
        num = num2 = 0
        for digit in date:
            num += int(digit)
        for i in str(num):
                num2 += int(i)
        return num2
    
date = str(input('Enter the date: '))
print("The digit of life is: ",digitoflife(date))

# LAB 5 LETTER IN A STRIN

Random = "Messi is the best soccer player in the world"
words2 = Random.split(" ")

print(len(Random))
#letters there are

def containsAny(str, set):
    """ Check whether sequence str contains ANY of the items in set. """
    if str.find(set) != -1: return True
    else: print("not inside string set")

def containsAll(str, set):
    """ Check whether sequence str contains ALL of the items in set. """
    return 0 not in [c in str for c in set]

containsAll(Random, 'play')

containsAny(Random, 'an')

# LAB 6 SUDOKU

board = [
    [0, 0, 0, 8, 0, 0, 4, 0, 3],
    [2, 0, 0, 0, 0, 4, 8, 9, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 2, 9, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 6, 5, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 6, 2, 7, 0, 0, 0, 0, 1],
    [4, 0, 3, 0, 0, 6, 0, 0, 0]
]

def isPossible(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == board[i][j-1]:
                return False
    
    for j in range(9):    
        for i in range(9):
            if board[i][j] == board[i-1][j]:
                return False

    return True

isPossible(board)


b1 = [[2,9,5,7,4,3,8,6,1],
[4,3,1,8,6,5,9,2,7],
[8,7,6,1,9,2,5,4,3],
[3,8,7,4,5,9,2,1,6],
[6,1,2,3,8,7,4,9,5],
[5,4,9,2,1,6,7,3,8],
[7,6,3,5,2,4,1,8,9],
[9,2,8,6,7,1,3,5,4],
[1,5,4,9,3,8,6,7,2]]

isPossible(b1)