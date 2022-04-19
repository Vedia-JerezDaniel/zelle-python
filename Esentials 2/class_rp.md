Like many other programming languages, Python supports [object-oriented programming](https://realpython.com/python3-object-oriented-programming/). At the heart of Python’s object-oriented capabilities, you’ll find the [`class`](https://realpython.com/python-keywords/#structure-keywords-def-class-with-as-pass-lambda) keyword, which allows you to define custom classes that can have [attributes](https://realpython.com/python3-object-oriented-programming/#class-and-instance-attributes) for storing data and [methods](https://realpython.com/python3-object-oriented-programming/#instance-methods) for providing behaviors.

Creating and initializing objects of a given class is a fundamental step in object-oriented programming. This step is often referred to as **object construction** or **instantiation**. The tool responsible for running this instantiation process is commonly known as a **class constructor**.

### Understanding Python’s Instantiation Process

You trigger Python’s **instantiation process** whenever you call a Python class to create a new instance. This process runs through two separate steps, which you can describe as follows:

1. **Create a new instance** of the target class
2. **Initialize the new instance** with an appropriate initial [state](https://en.wikipedia.org/wiki/State_(computer_science))

To run the first step, Python classes have a special method called [`.__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__), which is responsible for creating and returning a new empty object. Then another special method, [`.__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__), takes the resulting object, along with the class constructor’s arguments.

Here’s a breakdown of what this code does:

- **Line 3** defines the `Point` class using the `class` keyword followed by the class name.

- **Line 4** defines the `.__new__()` method, which takes the class as its first argument. Note that using `cls` as the name of this argument is a strong convention in Python, just like using `self` to name the current instance is. The method also takes [`*args` and `**kwargs`](https://realpython.com/python-kwargs-and-args/), which allow for passing an undefined number of initialization arguments to the underlying instance.

- **Line 5** [prints](https://realpython.com/python-print/) a message when `.__new__()` runs the object creation step.

- **Line 6** creates a new `Point` instance by calling the parent class’s `.__new__()` method with `cls` as an argument. In this example, [`object`](https://docs.python.org/3/library/functions.html#object) is the parent class, and the call to [`super()`](https://realpython.com/python-super/) gives you access to it. Then the instance is returned. This instance will be the first argument to `.__init__()`.

- **Line 8** defines `.__init__()`, which is responsible for the initialization step. This method takes a first argument called `self`, which holds a reference to the current instance. The method also takes two additional arguments, `x` and `y`. These arguments hold initial values for the instance attributes `.x` and `.y`. You need to pass suitable values for these arguments in the call to `Point()`, as you’ll learn in a moment.

- **Line 9** prints a message when `.__init__()` runs the object initialization step.

- **Lines 10 and 11** initialize `.x` and `.y`, respectively. To do this, they use the provided input arguments `x` and `y`.

- **Lines 13 and 14** implement the [`.__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__) special method, which provides a proper string representation for your `Point` class.

  

- ```python
  # point.py
  
  class Point:
      def __new__(cls, *args, **kwargs):
          print("1. Create a new instance of Point.")
          return super().__new__(cls)
  
      def __init__(self, x, y):
          print("2. Initialize the new instance of Point.")
          self.x = x
          self.y = y
  
      def __repro__(self) -> str:
          return f"{type(self).__name__}(x={self.x}, y={self.y})"
      
      
  a = Point(1, 2)
  a.__repro__()
  ```

  