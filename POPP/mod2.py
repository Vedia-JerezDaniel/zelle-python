# ADDING CORE PYTHON SYNTAX

class Person:
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary

    def __add__(self, other):
        return self.weight + other.weight

p1 = Person(30, 40, 50)
p2 = Person(35, 45, 55)

print(p1 + p2)

# INHERITANCE MULTIPLE

class MFD:
    def __init__(self, scan, printe, send):
        self.scan = scan
        self.print = printe
        self.send = send

class Scanner:
    def __init__(self, scan):
        return scan
    
class Printer:
    def __init__(self, printe):
        return printe
    
class Fax:
    def __init__(self, send, printe):
        return send if send == True else printe
        
p1 = MFD(0,1,1)
p2 = MFD(1,0,1)

p1.scan
p1.print


# POLYMORPHISM

class Device:
    def turn_on(self):
        print('The device was turned on')

class Radio(Device):
    pass

class PortableRadio(Device):
    def turn_on(self):
        print('PortableRadio type object was turned on')

class TvSet(Device):
    def turn_on(self):
        print('TvSet type object was turned on')

device = Device()
radio = Radio()
portableRadio = PortableRadio()
tvset = TvSet()

for element in (device, radio, portableRadio, tvset):
    element.turn_on()

# inheritance: class Radio inherits the turn_on() method from its superclass
# — that is why we see The device was turned on string twice. Other subclasses 
# override that method and as a result we see different lines being printed;
# polymorphism: all class instances allow the calling of the turn_on() 
# method, even when you refer to the objects using the arbitrary variable element

class Wax:
    def melt(self):
        print("Wax can be used to form a tool")

class Cheese:
    def melt(self):
        print("Cheese can be eaten")

class Wood:
    def fire(self):
        print("A fire has been started!")

for element in Wax(), Cheese(), Wood():
    try:
        element.melt()
    except AttributeError:
        print('No melt() method')
        
# DECORATORS

def simple_hello():
    print("Hello from simple function!")
    
def simple_decorator(function):
    print(f'We are about to call "{function.__name__}"')
    return function

decorated = simple_decorator(simple_hello)
decorated()

# Now let's create another function, simple_decorator(), which is more 
# interesting as it accepts an object as a parameter, displays 
# a __name__ attribute value of the parameter, and returns an accepted object.

@simple_decorator
def simple_hello():
    print("Hello from simple function!")
