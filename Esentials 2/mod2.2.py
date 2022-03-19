# Exceptions: continued

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")

# --2.6.1.10 Errors 
print("alpha"[1/0])

def face(x):
    assert x
    return 1/x

print(face(0))

from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))

# We must be sure that angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))

# The code shows an extravagant way
# of leaving the loop.

the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True

while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False

print('Done')


# How to abuse the dictionary
# and how to deal with it?

dictionary = { 'a': 'b', 'b': 'c', 'c': 'd' }
ch = 'a'

try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)

# LAB 1 EXCEPTIONS

def read_int(prompt, min, max):
    x = range(min, max)
    prompt = int(input("Enter a number from -10 to 10: "))
    try:
        if prompt in x:
            print('The number is:', prompt)
    except (TypeError, ValueError):
        print("Error wrong input.")
    try:
        if x[prompt]:
            print('The value os this position is:', x[prompt])
    except IndexError:
        print("Error: the value is not within permitted range (min..max)")


v = read_int("Enter a number from -10 to 10: ", -10, 10)

v = 'd'
try:
    assert int(v)
    11/v  # type: ignore
except ValueError:
        print("Error wrong input.")

# TEST PART TWO

v.isalnum()

'Mike' > 'Mikey'

#  MODULE TEST PART TWO

try:
    print('5'/0)
except ArithmeticError:
    print('art')
except ZeroDivisionError:
    print('zero')
except:
    print('something')

print(ord('c')- ord('a'))

print(float("1, 3"))

print(3 * 'abc'+'xyz')

var = 0
assert var == 0
print(1/var)

x = '\''
print(len(x))

print(chr(ord('z')- 2))