stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

# The object approach: a stack from scratch

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())

# Adding Subclases
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
        
    def get_sum(self):
        return self.__sum

stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())
    
# LAB 1 Stack counter

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        Stack.__counter = 0

    def pop(self):
        val = Stack.pop(self)
        self.__counter -= val
        return val

    def get_counter(self):
        return self.__counter + 5050

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())

# LAB 2 FIFO

class Queue:
    def __init__(self):
        self.stack = []

    def put(self, elem):
        self.stack.append(elem)
    
    def get(self):
        elem = self.stack[-1]
        del self.stack[-1]
        return elem

que = Queue()
que.put(1)
que.put("dog")
que.put(False)

try:
    for _ in range(4):
        print(que.get())
except:
    print("Queue error")
    
#  LAB 3 SUPERCLASS QUE

class Queue:
    def __init__(self):
        self.stack = []

    def put(self, elem):
        self.stack.append(elem)
    
    def get(self):
        if len(self.stack) != 0:
            elem = self.stack[-1]
            del self.stack[-1]
            return elem
  
class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        
    def put(self, elem):
        Queue.put(self, elem)
        
    def get(self):
        return Queue.get(self)
    
    def isempty(self):
        if self.stack == []:
            print("Queue empty")   
    

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
        
# METHODS IN DETAILS

class Classy:
    def method(self, par):
        print("method:", par)

obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)


class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()

obj = Classy()
obj.method()

# access to invisible variables
class Classy:
    def visible(self):
        print("visible")
    
    def __hidden(self):
        print("hidden")


obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

obj._Classy__hidden()

# LAB 1 to LAB 4
# are impossible to me

# INHERITANCE
class Super:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Hello My name is {self.name}."

class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)

obj = Sub("Dany")

print(obj)

# using the super() function
class Super:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Hello My name is {self.name}."

class Sub(Super):
    def __init__(self, name):
        super().__init__(name)

obj = Sub("Dan")
print(obj)

# Testing properties: class variables.
class Super:
    superVar = 12

class Sub(Super):
    subVar = 16

obj = Sub()

print(obj.subVar)
print(obj.superVar)

# Example of a class variable
class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101
    def fun_1(self):
        return 102

class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    def fun_2(self):
        return 202

class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301
    def fun_3(self):
        return 302
    
class Level4(Level3):
    variable_4 = 400
    def __init__(self):
        super().__init__()
        self.var_4 = 401
    def fun_4(self):
        return 402

obj = Level4()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())
print(obj.variable_4, obj.var_4, obj.fun_4())


class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return f'{self.breed} says: Woof!'

class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " Don't run away, Little Lamb!"

class GuardDog(Dog):
    def __str__(self):
        return f'{super().__str__()} Stay where you are, Mister Intruder!'


rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")

print(rocky)
print(luna)

print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))

print(rocky.kennel)

# MODULE 3 TEST

import math

try:
    print(math.pow(2))
except TypeError:
    print('A')
else:
    print('B')	

# FINAL MODULE 3 TEST
class A:
    A = 1
    
print(hasattr(A, 'A'))


class Class:
    def __init__(self):
        pass

o = Class
print(o)

def f(x):
    try: x = x/x
    except: print('A', end='')
    else: print('B', end='')
    finally: print('C', end='')
    
f(1)
f(0)

class  A:
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
    def __init__(self):
        self.a = 1
    
class B(A):
    def __init__(self):
        A.__init__(self)  
        self.b = 2

o = B()


class A:
    def __init__(self, v=1):
        self.v = v
        
    def set(self, v):
        self.v = v
        return v
    
a = A()
print(a.set(a.v +1))

class A:
    def __init__(self, v):
        self.__a = v+1
        
a = A(0)
print(a.__a)

try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))
    
class A:
    v=2
    
class B(A):
    v = 1
    
class C(B):
    pass

o = C()
print(o.v)

class A:
    def __str__(self):
        return 'a'
class B():
    def __str__(self):
        return 'b'
    
class C(A,B):
    pass

o = C()
print(o)

class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.args = (msg,)
        
try: raise Ex('ex')
except Ex as e: print(e)
except Exception as e: print(e)

class A:
    X = 0
    def __init__(self, v=0):
        self.Y = v
        A.X +=v
        
a = A()
b = A(1)
c = A(2)
print(c.X)


class A:
    pass
class B(A):
    pass
    
class C(B):
    pass

print(issubclass(C, A))