# point.py

class Point:
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Point.")
        return super().__new__(cls)

    def __init__(self, x, y):
        print("2. Initialize the new instance of Point.")
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        print('The sum of x and y is: ', self.x + self.y)
        return f"{type(self).__name__}(x={self.x}, y={self.y})"
       
    
    
a = Point(1, 2)
print(a)

b = Point.__new__(Point)
b.__init__(4,5)
b


# ab_classes.py

class A:
    def __init__(self, a_value):
        print("Initialize the new instance of A.")
        self.a_value = a_value

class B:
    def __new__(self, *args, **kwargs):
        return A(56).__new__(self)

    def __init__(self, b_value):
        print("Initialize the new instance of B.")
        self.b_value = b_value
        
b = B(1)
b.__init__(200)
b.b_value

a = A(100)
a.a_value

https://realpython.com/python-class-constructor/#pythons-class-constructors-and-the-instantiation-process

class Rectangle:
    def __init__(self, width, height):
        if not (isinstance(width, (int, float)) and width > 0):
            raise ValueError(f"positive width expected, got {width}")
        self.width = width
        if not (isinstance(height, (int, float)) and height > 0):
            raise ValueError(f"positive height expected, got {height}")
        self.height = height
        
rec = Rectangle(10, 20)
rec.width

# Now say that you’re using inheritance to create a custom class hierarchy and reuse some functionality in your code. If your subclasses provide a.__init__() method, then this method must explicitly call the base class’s .__init__() method with appropriate arguments to ensure the correct initialization of instances. To do this, you should use the built-in super() function

class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

class Employee(Person):
    def __init__(self, name, birth_date, position):
        super().__init__(name, birth_date)
        self.position = position

john = Employee("John Doe", "2001-02-07", "Python Developer")

john.name
john.birth_date
john.position

