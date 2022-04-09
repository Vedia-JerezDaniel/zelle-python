# GENERATORS

class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in {1, 2}:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)
    

class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in {1, 2}:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter;

object = Class(8)
for i in object:
    print(i)


def fun(n):
    yield from range(n)

for i in fun(5):
    print(i)
    

def powers_of_2(n):
    power = 1
    for _ in range(n):
        yield power
        power *= 2

t = list(powers_of_2(5))
print(t)

# List comprehensions

list_1 = [12 ** ex for ex in range(2)]
list_2 = [10 ** ex for ex in range(6)]

print(list_1)
print(list_2)

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
print(the_list)

# Using generators there is no list
for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()

# Lambda expressions
def print_function(args, fun):
    for x in args:
        print('f(', x,') = ', fun(x), sep='')

print_function(list(range(-2, 3)), lambda x: 2 * x**2 - 4 * x + 2)

# Map
list_1 = list(range(5))

list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

list_3 = list(map(lambda x: x * x, list_2))
print(list_3)

# Filter
from random import  randint

data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

# Closures

def outer(par):
    loc = par

    def inner():
        return loc
    return inner

var = 2
fun = outer(var)
dir(fun)
print(fun())

def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power

fsqr = make_closure(2)
print(fsqr(2))
fcub = make_closure(3)
qcubert = make_closure(4)

for i in range(5):
    print(i, fsqr(i), fcub(i), qcubert(i))

# FILE PROCESSING
import errno

file ='E:/GitRepo/CB speeches/BOE/Bailey/copy/20/20/r210604.txt'
try:
    with open(file, mode = 'rt', encoding = 'utf-8') as stream:
        dir(stream)
        stream.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)
    


