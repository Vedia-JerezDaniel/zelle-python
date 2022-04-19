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
    

#   WORKING WITH REAL FILES
from os import strerror

try:
    cnt = 0
    s = open(file, "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))
    
# USING READLINE

try:
    ccnt = lcnt = 0
    s = open(file, 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    

# LAB 1

from os import strerror
try:
    src = open(file, 'rt')
except IOError as e:
    print("Cannot open the file: ",strerror(e.errno))
    
alpha = 'abcdefghijklmnopqrstuvwxyz'
dataDict ={}
for letter in alpha:
    dataDict.update({letter:0})
    
data = src.read().strip()
data2 = data.lower()

for ch in data2:
    if ch.isalpha():
        temp = {ch:dataDict[ch]+1}
        dataDict.update(temp)

for i in alpha:
    if dataDict[i] > 0:
        print(i,' -> ', dataDict[i])
        
src.close()

# LAB 2: SORTED using LAMBDA

from os import strerror

try:
    src = open(file, 'rt')
except IOError as e:
    print("Cannot open the file: ",strerror(e.errno))
    
alpha = 'abcdefghijklmnopqrstuvwxyz'
dataDict ={}
for letter in alpha:
    dataDict.update({letter:0})
    
data = src.read().strip()
data2 = data.lower()

for ch in data2:
    if ch.isalpha():
        temp = {ch:dataDict[ch]+1}
        dataDict.update(temp)

# ======================================================

valueList = list(dataDict.values())
valueList.sort()
sortedValue = list(filter(lambda x: x > 0, valueList))

acendValue = []
for i in range(0,len(sortedValue)):
    acendValue.append(sortedValue.pop())

for item in acendValue:
    for letter in list(dataDict.keys()):
        if dataDict[letter] == item:
            print(letter, ' -> ', item)
            newData = letter + ' -> ' + str(item) + '\n'
            del dataDict[letter]
            
src.close()


# LAB 3  NOTES

class StudentsDataException(BaseException):
    pass 

class BadLine(StudentsDataException):
    def __str__ (self):
        return "There is bad lines or wrong scores." 

class FileEmpty(StudentsDataException):
    def __str__ (self):
        return "There is no data in the file." 

def closeFilesAndExit(src, e):
    src.close()
    return e.__str__()

mark = 'grade.txt'
try:
    with open(mark, 'rt') as src:
        data = src.readlines()
        if data == []:
            raise FileEmpty()
        try:
            studentDict = {}
            for i in data:
                newData = i.strip().replace('\t',' ')
                studentData = newData.split(' ')
                student = f'{studentData[0]} {studentData[1]}'
                studentOneScore = studentData[2]
                if student in studentDict:
                    temp = {student: float(studentDict[student])+float(studentOneScore)}
                else:
                    temp = {student: float(studentOneScore)}
                studentDict.update(temp)

            for k in sorted(studentDict.keys()):
                temp = k + str(studentDict[k]) + '\n'
        except:
            raise BadLine()

except FileEmpty as fe:
    message = closeFilesAndExit(src, fe)
    print(message)
except BadLine as bl:
    message = closeFilesAndExit(src, bl)
    print(message)
except BaseException as e:
    message = closeFilesAndExit(src, e)
    print(message)


# LAB OS

import os

os.makedirs("tree/c/other courses/cpp")
os.makedirs("tree/c/other courses/python")
os.makedirs("tree/cpp/other courses/c")
os.makedirs("tree/cpp/other courses/python")
os.makedirs("tree/python/other courses/cpp")
os.makedirs("tree/python/other courses/c")

print(os.getcwd())
os.chdir("tree")
print(os.getcwd())
print(os.listdir('python'))
print(os.walk('python'))

import os
from os.path import join, getsize
for root, dirs, files in os.walk('E:\\GitRepo\\zelle-python\\Esentials 2\\tree'):
    print("bytes in", len(files), "non-directory files")
    if 'python' in dirs:
        print(root)
        

# Introduction to the datetime module

from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)


t = time(14, 53, 20, 1)
print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)

# Timestamp
from datetime import datetime

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())

# Operations

from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)
print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)
print(dt1 - dt2)

from datetime import timedelta
delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)

# LAVB

from datetime import datetime
date = datetime(2020,11,4,14,53)

print(date.strftime("%Y/%m/%d %H:%M:%S"))
print(date.strftime("%Y/%m/%d %H:%M:%S %p"))
print(date.strftime("%a, %Y, %b, %d"))
print(date.strftime("%A, %Y %b %d"))
print(date.strftime("Weekday: %A: %d"))
print(date.strftime("Day of the year: %j"))
print(date.strftime("Week number of the year: %W"))

# THE CALENDAR MODULE
import calendar
class mycal(calendar.Calendar):
    def count_weekday(self,year, weekday):
        number_days = 0
        for current_month in range(1, 13):
            for i in self.monthdays2calendar(year, current_month):
                if i[weekday][0] != 0:
                        number_days += 1
            current_month += 1
        return number_days

cal = mycal()
numdays = cal.count_weekday(2000, calendar.SUNDAY)
print(numdays)

# MODULE 4 QUIZ

def fun():
    for i in range(3):
        yield i
        
for i in fun():
    print(i)    
    
foo = [i + i for i in range(5)]
print(fo)

x = lambda a, b : a**b
print(x(2,10))


num = (1,2,5,9,15)

def fil(m):
    nums = (1,5,17)
    return i in nums

filter_num = filter(fil, num)
for i in filter_num:
    print(i)

import os
os.mkdir('a/b/c/d')

import time

time.sleep(30)

import calendar
cal = calendar.isleap(2019)
print(cal)

# MODULE 4 TEST

os.mkdir('thumbnails')
os.chdir('thumbnails')

se = ['small','medium','large']

for s in se:
    os.mkdir(s)
print(os.listdir())


tu = (0,1,2,3,4,5,6)
foo = list(filter(lambda x: x-0 and x-1, tu))
print(foo)


b = bytearray(3)
print(b)

c = calendar.Calendar()
for w in c.iterweekdays():
    print(w, end=" ")
    
    
def I():
    s = 'abcdef'
    for c in s[::2]:
        yield c
        
for x in I():
    print(x, end="")
    
    
def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s
        
for x in fun(2):
    print(x, end="")
    
    
from datetime import datetime
datetime = datetime(2019, 11, 27,11, 27, 22)
print(datetime.strftime('%y/%B/%d %H:%M:%S'))

print(calendar.weekheader(2))

from datetime import date

da = date(1992,1,16)
sa= date(1991,2,5)

print(da-sa)

def o(p):
    def q():
        return '*' * p
    return q

r = o(1)
s = o(2)

print(r() + s())

my = [1,2,3]
foo = list(map(lambda x: x**x, my))
print(foo)


os.mkdir('pictures')
os.chdir('pictures')
os.mkdir('thumbnails')
os.chdir('thumbnails')
os.mkdir('temp')
os.chdir('../')

print(os.getcwd())

# FINAL TEST

from datetime import timedelta
delta = timedelta(weeks=1, days=7, hours=11)
print(delta *2)

v = 2
assert v != 0

class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1    
        return v

for x in I():
    print(x, end="")
    
x = "\\\\"
print(len(x))

import calendar

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.weekheader(3))


from datetime import datetime
da1 = datetime(2019, 11, 27, 11, 27, 22)
sa = datetime(2019, 11, 27, 0, 0, 0)

print(da1- sa)

try:
    raise Exception
except BaseException: print('a')
except Exception: print('b')
except: print('c')

try:
    raise Exception
except: print('c')
except BaseException: print('a')
except Exception: print('b')



class A:
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')
        
class C(B,A):
    def c(self):
        self.a()
        
o = C()
o.c()


class A:
    pass
class B(A):
     pass
class C(B):
    pass
        
print(issubclass(A,C))


class A:
    A = 1
    def __init__(self):
        self.a  = 0
    
# a = A(0)
print(hasattr(A, 'a'))

num = [0,2,7,9,10]
foo = map(lambda x: x**2, num)
print(list(foo))

import math
print(dir(math))

def my(n):
    s = '+'
    for i in range(n):
        s += s
        yield s
        
for x in my(2): 
    print(x, end="")
    
    
def o(p):
    def q():
        return '*' * p
    return q

r = o(1)
s = o(2)
print(r() + s())


class Class:
    def __init__(self, val=0):
        pass
    
o = Class(None)    

num = [i*i for i in range(5)]
foo = list(filter(lambda x: x%2, num))
print(foo)


import random

a = random.randint(0,100)
c = random.randrange(10,100,3)
b = random.choice((10,100,3))

print(a,b,c)

class A:
    def __init__(self, v =2):
        self.v = v
        
    def set(self, v=1):
        self.v += v
        return self.v
    
a = A()
b = a
b.set()
print(a.v)

print(float('1.3'))
print(chr(ord('p')+2))

from math import sin
math.sin(5)

try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))