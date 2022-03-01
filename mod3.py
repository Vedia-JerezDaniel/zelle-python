odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

## EX1
sn = 16
val = eval(input('Choose your number: '))
while val != sn:
    print("your are inside the loop")
    val = eval(input('Choose your number: '))
    if val == sn:
        print('Congratulations free to go')

# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

largest_number = -99999999
counter = 0

# The break instruction
while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0: print("The largest number is", largest_number)
else: print("You haven't entered any number.")

## EX2
while True:
    word = (input("Enter a word /'chupacabra' to left the loop: "))
    if word == 'chupacabra':
        break

    print("You haven't left the loop.")
if word == 'chupacabra': print("You've successfully left the loop.")

## EX3
vowels ='AEIOU'
word = input("Enter a word: ").upper()
not_eaten = [i for i in word if i not in vowels]

print(not_eaten)
i = 111
for i in range(2, 1):
    print(i)
print("else:", i)

# EX4

blocks = int(input("Enter number of blocks: "))

for n in range(blocks): 
    if n*(n+1)/2 <= blocks: 
        height = n

print("The height of the pyramid is:",height)


#EX 5
c0 = int(input("Enter a number non-negative: "))
steps = 0
while c0 != 1:
    if c0 % 2 == 0: 
        c0 /= 2
    else: 
        c0 = (3 * c0) + 1
    steps += 1
    print(c0)
print("steps: ", steps)


for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
        

i = 15
j = 22

log = i and j
bit = i & j
logneg = not i
the_mask = 8

# LISTS
hat_list = [1, 2, 3, 4, 5]

hat_list[2] = eval(input("enter a number: "))

hat_list.pop(-1)

# LAB 2 for LIsts
beatles = []
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')

print(beatles)

for i in range(2):
    i = input('Enter the next band member: ')
    beatles.append(i)

del beatles[3]
del beatles[3]

beatles.insert(3,'Ringo Star')

# Sorting list
my_list = [8, 10, 6, 2, 4]  

for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] 

print(my_list)

# Version 2

swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

# LAB

my_list = [8, 10, 6, 2, 4, 12, 45]
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

# Largest
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)


my_list = [1, 2, 3, 12, 16, 45, 6, 7, 8, 9, 10]
to_find = 45
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found: # es igual a Found = True
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

# LAB

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
temp = []

for i in my_list:
    if i not in temp:
        temp.append(i)

print("The list with unique elements only:")
print(temp)


list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)
# List in lists

board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
    
# Chess board
    
board = [[0 for i in range(8)] 
         for j in range(8)]

temps = [[0.0 for h in range(24)] for d in range(31)]

import numpy as np
np.shape(temps)

# hours in a day

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

# only days in temps
hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")

# Three-dimensional arrays

rooms = [[[False for r in range(20)] 
          for f in range(15)] 
         for t in range(3)]

np.shape(rooms)

# Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors each. There are 20 rooms on each floor. For this, you need an array which can collect and process information on the occupied/free rooms.


# Check if there are any vacancies on the 15th floor of the third building:
# The vacancy variable contains 0 if all the rooms are occupied, or the number of available rooms otherwise.

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
        
cubed = [num ** 3 for num in range(5)]
print(cubed)  

my = [[0,1,2,3] for num in range(2)]
for i in range(len(my)):
    my.insert(1,my[i])
  
print(my[2][0])
my

my.insert(0,1)
del my[1]
v = my[-1:-2]

print(my[-3:-2])

v = my

del v[1:2]

my[0], my[2] = my[2] , my[0]

for i in my:
    mu.insert(0,i)
print(mu)

t = [[3-i for i in range(3)] for j in range(3)]
s= 0
for i in range(3):
    s += t[i][i]
print(s) 

v = 1
while v <10:
    # v += 1
    # if v % 2 == 0:
    #     continue
    print('#')
    v = v << 1
    
for i in range(1):
    print('#')
else:
    print('#')
    
z = 10
y =0
x = y < z and z > y or y > z and z <y

a =1
b=0
c = a&b
d = a| b
e = a ^b
print(c+d+e)

i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print('#')
    
    
my  = [i for i in range(-1,2)]
my

x = 1
x = x == x
x

def add(a, b, c):
    print(a + b + c)


add(a=1, c=3)


def strange_function(n):
    return (n % 2 == 0)

print(strange_function(7))


def strange_list_fun(n):
    strange_list = []
    for i in range(n):
        strange_list.insert(1, i)
    return strange_list

print(strange_list_fun(5))

# LAB 1 Module 4

def is_year_leap(year):
    if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"-> ", end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
  
  # LAB 2 Module 4
  
def is_year_leap(year):
    if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        return True

def days_in_month(year, month):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month == 2:
        return 29 if is_year_leap(year) else 28
    return 30

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "-> ", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
  
  # LAB 3
  
def is_year_leap(year):
    if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        return True

def days_in_month(year, month):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month == 2:
        return 29 if is_year_leap(year) else 28
    return 30

def day_of_year(year, month, day):
    """ given year, month, day return day of year
        Astronomical Algorithms, Jean Meeus, 2d ed, 1998, chap 7 """
    K = 1 if is_year_leap(year) else 2
    return int((275 * month) / 9.0) - K * int((month + 9) / 12.0) + day - 30

print(day_of_year(2019, 2, 10))
  
# LAB 4

def is_prime(num):
    return all(num%n != 0 for n in range(2, int(num**1/2)+1))
    
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")

# LAB 5

def liters_100km_to_miles_gallon(liters):
    """1 American mile = 1609.344 metres;
       1 American gallon = 3.785411784 litres.
    """
    km_m = 100/1.609344
    l_g = 1/3.785411784
    return km_m/(liters*l_g)

def miles_gallon_to_liters_100km(miles):
    m_km = (1.609344/100)*miles
    g_l = 3.785411784
    return g_l/m_km


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


## Tuples and dictionaries can work together

school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break

    score = int(input("Enter the student's score (0-10): "))
    if score not in range(11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
    
    
my_tuple = (5, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)

tup = 1, 2, 3,
a, b, c = tup

print(a * b * c)


d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)


# EXCEPTIONS
short_list = [1]
one_value = short_list[0]

dir(short_list) # to see attributes of objects


while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Wrong value or No division by zero rule broken.")
    except:
        print("Sorry, something went wrong...")


bin(4 ^ 1)
x=15
y = 16
bin(y<<1) 

import numpy as np
rooms = [[[False for r in range(20)] 
         for f in range(15)] 
         for t in range(3)]

np.shape(rooms)


