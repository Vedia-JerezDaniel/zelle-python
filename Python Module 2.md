---
output:
  pdf_document: default
  html_document: default
---
# Python Institute

___

## First course for PEPP

***

## **Data types, variables, basic input-output operations, basic operators**

### Functions

Let's see:

- First, Python checks if the name specified is **legal** (it browses its internal data in order to find an existing function of the name; if this search fails, Python aborts the code);
- second, Python checks if the function's requirements for the number of arguments **allows you to invoke** the function in this way (e.g., if a specific function demands exactly two arguments, any invocation delivering only one argument will be considered erroneous, and will abort the code's execution);
- third, Python **leaves your code for a moment** and jumps into the function you want to invoke; of course, it takes your argument(s) too and passes it/them to the function;
- fourth, the function **executes its code**, causes the desired effect (if any), evaluates the desired result(s) (if any) and finishes its task;
- finally, Python **returns to your code** (to the place just after the invocation) and resumes its execution.



### Operators priority

Look at the table below:

| Priority | Operator            |        |
| :------- | :------------------ | :----- |
| 1        | `+`, `-`            | unary  |
| 2        | `**`                |        |
| 3        | `*`, `/`, `//`, `%` |        |
| 4        | `+`, `-`            | binary |



### Key takeaways

1. An **expression** is a combination of values (or variables, operators, calls to functions - you will learn about them soon) which evaluates to a value, e.g., `1 + 2`.

2. **Operators** are special symbols or keywords which are able to operate on the values and perform (mathematical) operations, e.g., the `*` operator multiplies two values: `x * y`.

3. Arithmetic operators in Python: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (classic division - always returns a float), `%` (modulus - divides left operand by right operand and returns the remainder of the operation, e.g., `5 % 2 = 1`), `**` (exponentiation - left operand raised to the power of right operand, e.g., `2 ** 3 = 2 * 2 * 2 = 8`), `//` (floor/integer division - returns a number resulting from division, but rounded down to the nearest whole number, e.g., `3 // 2.0 = 1.0`)

4. A **unary** operator is an operator with only one operand, e.g., `-1`, or `+3`.

5. A **binary** operator is an operator with two operands, e.g., `4 + 5`, or `12 % 5`.

6. Some operators act before others - **the hierarchy of priorities**:

- unary `+` and `-` have the highest priority
- then: `**`, then: `*`, `/`, and `%`, and then the lowest priority: binary `+` and `-`.

7. Subexpressions in **parentheses** are always calculated first, e.g., `15 - 1 * (5 * (1 + 2)) = 0`.
8. The **exponentiation** operator uses **right-sided binding**, e.g., `2 ** 2 ** 3 = 256`.



### Writing programs

Writing programs requires a systematic approach to problem solving and involves the following steps: 

1. Problem Analysis: Studying the problem to be solved.

2. Program Specification: Deciding exactly what the program will do. 

3. Design: Writing an algorithm in pseudocode. 

4. Implementation: Translating the design into a programming language. 

5. Testing/Debugging: Finding and fixing errors in the program. 

6. Maintenance: Keeping the program up to date with evolving needs.

   

## Module 3

## Loops in Python

If you notice some similarities to the *if* instruction, that's quite all right. Indeed, the syntactic difference is only one: you use the word `while` instead of the word `if`.

The semantic difference is more important: when the condition is met, *if* performs its statements **only once**; *while* **repeats the execution as long as the condition evaluates to `True`**.

It is now important to remember that:

- if you want to execute **more than one statement inside one `while`**, you must (as with `if`) **indent** all the instructions in the same way;
- an instruction or set of instructions executed inside the `while` loop is called the **loop's body**;
- if the condition is `False` (equal to zero) as early as when it is tested for the first time, the body is not executed even once (note the analogy of not having to do anything if there is nothing to do);
- the body should be able to change the condition's value, because if the condition is `True` at the beginning, the body might run continuously to infinity - notice that doing a thing usually decreases the number of things to do).



### For loops

- note the *pass* keyword inside the loop body - it does nothing at all; it's an **empty instruction** - we put it here because the `for` loop's syntax demands at least one instruction inside the body (by the way - `if`, `elif`, `else` and `while` express the same thing)

**These two instructions are:**

- `break` - exits the loop immediately, and unconditionally ends the loop's operation; the program begins to execute the nearest instruction after the loop's body;
- `continue` - behaves as if the program has suddenly reached the end of the body; the next turn is started and the condition expression is tested immediately.

Both these words are **keywords**.

Now we'll show you two simple examples to illustrate how the two instructions work. Look at the code in the editor. Run the program and analyze the output. Modify the code and experiment.

Both and and or distribute over each other. 

- a or (b and c) == (a or b) and (a or c) 
- a and (b or c) == (a and b) or (a and c)

A double negative cancels out. 

- not(not a) == a 

The next two identities are known as DeMorgan’s laws. 

- not(a or b) == (not a) and (not b) 
- not(a and b) == (not a) or (not b)



#### AND

The result provided by the `and` operator can be determined on the basis of the **truth table**.

How should this be evaluated? Python follows a standard convention that the order of precedence from high to low is not, followed by __and__, followed by __or__.

If we consider the conjunction of `A and B`, the set of possible values of arguments and corresponding values of the conjunction looks as follows:

| Argument `A` | Argument `B` | `A and B` |
| :----------- | :----------- | :-------- |
| `False`      | `False`      | `False`   |
| `False`      | `True`       | `False`   |
| `True`       | `False`      | `False`   |
| `True`       | `True`       | `True`    |

#### OR

A disjunction operator is the word `or`. It's a **binary operator with a lower priority than `and`** (just like `+` compared to `*`). Its truth table is as follows:

| Argument `A` | Argument `B` | `A or B` |
| :----------- | :----------- | :------- |
| `False`      | `False`      | `False`  |
| `False`      | `True`       | `True`   |
| `True`       | `False`      | `True`   |
| `True`       | `True`       | `True`   |

**Bitwise operations (**`&`**,** `|`**, and** `^`**)**

| Argument `A` | Argument `B` | `A & B` | ` A | B` | `A ^ B` |
| :----------- | :----------- | :------ | :------- | :------ |
| `0`          | `0`          | `0`     | `0`      | `0`     |
| `0`          | `1`          | `0`     | `1`      | `1`     |
| `1`          | `0`          | `0`     | `1`      | `1`     |
| `1`          | `1`          | `1`     | `1`      | `0`     |

Let's make it easier:

- `&` requires exactly two `1`s to provide `1` as the result;
- `|` requires at least one `1` to provide `1` as the result;
- `^` requires exactly one `1` to provide `1` as the result.

The **shift operators** in Python are a pair of **digraphs**: `<<` and `>>`, clearly suggesting in which direction the shift will act.

```
value << bits value >> bits 
```

**The left argument of these operators is an integer value whose bits are shifted. The right argument determines the size of the shift.**

And here is the **updated priority table**, containing all the operators introduced so far:

| Priority | Operator                                                     |        |
| :------- | :----------------------------------------------------------- | :----- |
| 1        | `~`, `+`, `-`                                                | unary  |
| 2        | `**`                                                         |        |
| 3        | `*`, `/`, `//`, `%`                                          |        |
| 4        | `+`, `-`                                                     | binary |
| 5        | `<<`, `>>`                                                   |        |
| 6        | `<`, `<=`, `>`, `>=`                                         |        |
| 7        | `==`, `!=`                                                   |        |
| 8        | `&`                                                          |        |
| 9        | `|`                                                          |        |
| 10       | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `^=`, `|=`, `>>=`, `<<=` |        |

### Key takeaways

1. Python supports the following logical operators:

- `and` → if both operands are true, the condition is true, e.g., `(True and True)` is `True`,
- `or` → if any of the operands are true, the condition is true, e.g., `(True or False)` is `True`,
- `not` → returns false if the result is true, and returns true if the result is false, e.g., `not True` is `False`.

2. You can use bitwise operators to manipulate single bits of data. The following sample data:

- `x = 15`, which is `0000 1111` in binary,
- `y = 16`, which is `0001 0000` in binary.

will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:

- `&` does a *bitwise and*, e.g., `x & y = 0`, which is `0000 0000` in binary,
- `|` does a *bitwise or*, e.g., `x | y = 31`, which is `0001 1111` in binary,
- `˜ ` does a *bitwise not*, e.g., `˜ x = 240`*, which is `1111 0000` in binary,
- `^` does a *bitwise xor*, e.g., `x ^ y = 31`, which is `0001 1111` in binary,
- `>>` does a *bitwise right shift*, e.g., `y >> 1 = 8`, which is `0000 1000` in binary,
- `<<` does a *bitwise left shift*, e.g., `y << 3 = `, which is `1000 0000` in binary,

`-16` (decimal from signed 2's complement) -- read more about the [Two's complement](https://en.wikipedia.org/wiki/Two's_complement) operation.

## Lists

![image-20220105164818251](/home/dani/.config/Typora/typora-user-images/image-20220105164818251.png)

In contrast, Python lists are dynamic. They can grow and shrink on demand. They are also heterogeneous. You can mix arbitrary data types in a single list. In a nutshell, Python lists are mutable sequences of arbitrary objects.

Because lists are sequences, you know that all of the Python built-in sequence operations also apply to lists. To jog your memory, here’s a summary of those operations: 



| Meaning       | Operator        |
| ------------- | --------------- |
| Concatenation | [seq] + [seq]   |
| Repetition    | [seq] * number  |
| Indexing      | [seq][][]       |
| Lenght        | len([seq])      |
| Slicing       | seq[:]          |
| Iteration     | for i in [seq]: |
| Membership    | expr in [seq]   |

```
# Remove
hat_list.pop(-1)
del hat_list[2]
# Insert
list.append(value)
list.insert(location, value)
```

###  List in lists (ist comprehension )

Let us show you some other **list comprehension examples**:

Example #1:

```
squares = [x ** 2 for x in range(10)] 
```

The snippet produces a ten-element list filled with squares of ten integer numbers starting from zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

Example #2:

```
twos = [2 ** i for i in range(8)] 
```

The snippet creates an eight-element array containing the first eight powers of two (1, 2, 4, 8, 16, 32, 64, 128)

Example #3:

```
odds = [x for x in squares if x % 2 != 0 ] 
```

#### Three-dimensional arrays

```
rooms = [[[False for r in range(20)] 
         for f in range(15)] 
         for t in range(3)]

np.shape(rooms)
```

*# Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors each. There are 20 rooms on each floor. For this, you need an array which can collect and process information on the occupied/free rooms.*

*# Check if there are any vacancies on the 15th floor of the third building:*

*# The vacancy variable contains 0 if all the rooms are occupied, or the number of available rooms otherwise.*

```
vacancy = 0
for room_number in range(20):
    if not rooms[2][14][room_number]:
       vacancy += 1
```

#### Summary for list

-  A list is a sequence of items stored as a single object. 
-  Items in a list can be accessed by indexing, and sublists can be accessed by slicing. 
- Lists are mutable; individual items or entire slices can be replaced through assignment statetments. 
- Lists support a number of convenient and frequently used methods. 
- Lists will grow and shrink as needed.

## Tupples and Dictionaries

A **sequence type is a type of data in Python which is able to store more than one value (or less than one, as a sequence may be empty), and these values can be sequentially (hence the name) browsed**, element by element.

As the `for` loop is a tool especially designed to iterate through sequences, we can express the definition as: **a sequence is data which can be scanned by the `for` loop**.

The second notion - **mutability** - is a property of any of Python's data that describes its readiness to be freely changed during program execution. There are two kinds of Python data: **mutable** and **immutable**.

**Mutable data can be freely updated at any time** - we call such an operation in situ.

*In situ* is a Latin phrase that translates as literally *in position*. For example, the following instruction modifies the data in situ:

```
list.append(1)
```

**Immutable data cannot be modified in this way**.

Imagine that a list can only be assigned and read over. You would be able neither to append an element to it, nor remove any element from it. This means that appending an element to the end of the list would require the recreation of the list from scratch.

The data type we want to tell you about now is a **tuple**. **A tuple is an immutable sequence type**. It can behave like a list, but it mustn't be modified in situ.

There are two tuples, both containing **four elements**.

Let's print them:

```
tuple_1 = (1, 2, 4, 8) 
tuple_2 = (1., .5, .25, .125)
print(tuple_1)
print(tuple_2)
```

What else can tuples do for you?

- the `len()` function accepts tuples, and returns the number of elements contained inside;
- the `+` operator can join tuples together (we've shown you this already)
- the `*` operator can multiply tuples, just like lists;
- the `in` and `not in` operators work in the same way as in lists.



### Dictionary

The **dictionary** is another Python data structure. It's **not a sequence** type (but can be easily adapted to sequence processing) and it is **mutable**.

To explain what the Python dictionary actually is, it is important to understand that it is literally a dictionary.

This means that a dictionary is a set of **key-value** pairs. Note:

- each key must be **unique** - it's not possible to have more than one key of the same value;
- a key may be **any immutable type of object**: it can be a number (integer or float), or even a string, but not a list;
- a dictionary is not a list - a list contains a set of numbered values, while a **dictionary holds pairs of values**;
- the `len()` function works for dictionaries, too - it returns the numbers of key-value elements in the dictionary;
- a dictionary is a **one-way tool** - if you have an English-French dictionary, you can look for French equivalents of English terms, but not vice versa.

```
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")
```

```python
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key]
```

##### How to use a dictionary: The items() and values() methods

Another way is based on using a dictionary's method named `items()`. The method **returns tuples** (this is the first example where tuples are something more than just an example of themselves) **where each tuple is a key-value pair**.

This is how it works:

```
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for english, french in dictionary.items():
	print(english, "->", french) 
```

There is also a method named `values()`, which works similarly to `keys()`, but **returns values**.

Here is a simple example:

```python
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"} 
for french in dictionary.values():    
	print(french)
```

##### How to use a dictionary: modifying and adding values

Assigning a new value to an existing key is simple - as dictionaries are fully **mutable**, there are no obstacles to modifying them.

We're going to replace the value `"chat"` with `"minou"`, which is not very accurate, but it will work well with our example

```
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"} 
dictionary['cat'] = 'minou' print(dictionary)
```

###### Adding a new key

Adding a new key-value pair to a dictionary is as simple as changing a value - you only have to assign a value to a new, **previously non-existent key**.

Note: this is very different behavior compared to lists, which don't allow you to assign values to non-existing indices.

Let's add a new pair of words to the dictionary - a bit weird, but still valid:

```
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"} 
dictionary['swan'] = 'cygne' print(dictionary)
```

**Update()**

```
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.update({"duck": "canard"})
print(dictionary)
```

**del()**

```
This is done with the del instruction.

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

del dictionary['dog']
print(dictionary)
```

**popitem()**

To remove the last item in a dictionary, you can use the `popitem()` method:

```
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"} 
dictionary.popitem()
print(dictionary)    
# outputs: {'cat': 'chat', 'dog': 'chien'} 
```

### Summary

\1. **Tuples** are ordered and unchangeable (immutable) collections of data. They can be thought of as immutable lists. They are written in round brackets:

\4. You can access tuple elements by indexing them:

```
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(my_tuple[3])  
# outputs: [3, 4] 
```

However, you can delete a tuple as a whole:

```
my_tuple = 1, 2, 3,  
del my_tuple
```

#### Key takeaways: dictionaries

 If you want to change the value associated with a specific key, you can do so by referring to the item's key name in the following way:

```
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

pol_eng_dictionary["zamek"] = "lock"
item = pol_eng_dictionary["zamek"]    
print(item)  # outputs: lock
```

You can also insert an item to a dictionary by using the `update()` method, and remove the last element by using the `popitem()` method, e.g.:

```
pol_eng_dictionary = {"kwiat": "flower"}

pol_eng_dictionary.update({"gleba": "soil"})
print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower', 'gleba': 'soil'}

pol_eng_dictionary.popitem()
print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower'}
```

If you want to loop through a dictionary's keys and values, you can use the `items()` method, e.g.:

**Delete and clear**

```python
print(len(pol_eng_dictionary))    # outputs: 3
del pol_eng_dictionary["zamek"]    # remove an item
print(len(pol_eng_dictionary))    # outputs: 2

pol_eng_dictionary.clear()   # removes all the items
print(len(pol_eng_dictionary))    # outputs: 0

del pol_eng_dictionary    # removes the dictionary
```











## Functions vs. methods

A **method is a specific kind of function** - it behaves like a function and looks like a function, but differs in the way in which it acts, and in its invocation style.

A **function doesn't belong to any data** - it gets data, it may create new data and it (generally) produces a result.

A method does all these things, but is also able to **change the state of a selected entity**.

**A method is owned by the data it works for, while a function is owned by the whole code**.

This also means that invoking a method requires some specification of the data from which the method is invoked.

It may sound puzzling here, but we'll deal with it in depth when we delve into object-oriented programming.

__In general, a typical function invocation may look like this:__

```
result = function(arg) 
```

The function takes an argument, does something, and returns a result.

__A typical method invocation usually looks like this:__

```
result = data.method(arg) 
```

Note: the name of the method is preceded by the name of the data which owns the method. Next, you add a **dot**, followed by the **method name**, and a pair of **parenthesis enclosing the arguments**.

The method will behave like a function, but can do something more - it can **change the internal state of the data** from which it has been invoked.

If the `start` specifies an element lying further than the one described by the `end` (from the list's beginning point of view), the slice will be **empty**:

```python
my_list = [10, 8, 6, 4, 2] 
new_list = my_list[-1:1] 
print(new_list) 
# The result is empty
```

### String methods

**Function 								**
s.capitalize() Copy of s with only the first character capitalized 									
s.center(width) Copy of s Centered s in a field of given width 									
s.count(sub) Count the number of occurrences of sub in s 									
s.find(sub) Find the first position where sub occurs in s 									
s.join(list) Concatenate list into a string, using s as separator 									
s.ljust(width) Like center, but s is left-justified 									
s.lower() Copy of s in all lowercase characters 									
s.lstrip() Copy of s with leading white space removed 									
s.replace(oldsub,newsub) Replace all occurrences of oldsub in s with newsub 



#### Format

Often, you’ll want to control the width and/or precision of a numeric value.

```
>>> "This int, {0:5}, was placed in a field of width 5".format(7)
’This int, 7, was placed in a field of width 5’
>>> "This int, {0:10}, was placed in a field of width 10".format(7)
’This int, 7, was placed in a field of width 10’
>>> "This float, {0:10.5}, has width 10 and precision 5".format(3.1415926)
’This float, 3.1416, has width 10 and precision 5’
>>> "This float, {0:10.5f}, is fixed at 5 decimal places".format(3.1415926)
’This float, 3.14159, is fixed at 5 decimal places’
>>> "This float, {0:0.5}, has width 0 and precision 5".format(3.1415926)
’This float, 3.1416, has width 0 and precision 5’
>>> "Compare {0} and {0:0.20}".format(3.14)
’Compare 3.14 and 3.1400000000000001243’

>>> "left justification: {0:<5}".format("Hi!")
’left justification: Hi! ’
>>> "right justification: {0:>5}".format("Hi!")
’right justification: Hi!’
>>> "centered: {0:^5}".format("Hi!")
’centered: Hi! ’
```

## Module 4. Functions

A good and attentive developer **divides the code** (or more accurately: the problem) into well-isolated pieces, and **encodes each of them in the form of a function**.

This considerably simplifies the work of the program, because each piece of code can be encoded separately, and tested separately. The process described here is often called **decomposition**.

We can now state the second condition: **if a piece of code becomes so large that reading and understating it may cause a problem, consider dividing it into separate, smaller problems, and implement each of them in the form of a separate function**.

This decomposition continues until you get a set of short functions, easy to understand and test.

- **parameters live inside functions** (this is their natural environment)
- **arguments exist outside functions**, and are carriers of values passed to corresponding parameters.

There is a clear and unambiguous frontier between these two worlds.



**At the end of every calculation function use _return_**.

There are two consequences of using **return**:

- it causes the **immediate termination of the function's execution** (nothing new compared to the first variant)
- moreover, the function will **evaluate the expression's value and will return (hence the name once again) it as the function's result**.

### Functions and scopes: the global keyword

Hopefully, you should now have arrived at the following question: does this mean that a function is not able to modify a variable defined outside it? This would create a lot of discomfort.

Fortunately, the answer is *no*.

There's a special Python method which can **extend a variable's scope in a way which includes the functions' bodies** (even if you want not only to read the values, but also to modify them).

Such an effect is caused by a keyword named `global`:

```python
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)

var = 1
my_function()
print(var)

```

## Exceptions

You can see two branches here:

- first, starting with the `try` keyword – this is the place where you put the code you suspect is risky and may be terminated in case of error; note: this kind of error is called an **exception**, while the exception occurrence is called **raising** – we can say that an exception is (or was) raised;
- second, the part of the code starting with the `except` keyword is designed to handle the exception; it's up to you what you want to do here: you can clean up the mess or you can just sweep the problem under the carpet (although we would prefer the first solution).

So, we could say that these two blocks work like this:

- the `try` keyword marks the place where you try to do something without permission;

- the `except` keyword starts a location where you can show off your apology talents.

    ```
    try:
        value = int(input('Enter a natural number: '))
        print('The reciprocal of', value, 'is', 1/value)        
    except ValueError:
        print('I do not know what to do.')    
    except ZeroDivisionError:
        print('Division by zero is not allowed in our Universe.')    
    except:
        print('Something strange has happened here... Sorry!')
    ```

    We've added a third `except` branch, but this time it **has no exception name specified** – we can say it's **anonymous** or (what is closer to its actual role) it's the **default**. You can expect that when an exception is raised and there is no `except` branch dedicated to this exception, it will be handled by the default branch.

    **Note:**

    

    **The default `except` branch must be the last `except` branch. Always!**













## Summary Zelle’s book

- A function is a kind of subprogram. Programmers use functions to reduce code duplication and to help structure or modularize programs. Once a function is defined, it may be calledmultiple times from many different places in a program. Parameters allow functions to have changeable parts. The parameters appearing in the function definition are called formal parameters, and the expressions appearing in a function call are known as actual parameters. 
- A call to a function initiates a four step process: 1. The calling program is suspended. 2. The values of actual parameters are assigned to the formal parameters. 3. The body of the function is executed. 4. Control returns immediately following the function call in the calling program. 
- The scope of a variable is the area of the program where it may be referenced. Formal parameters and other variables inside function definitions are local to the function. Local variables are distinct from variables of the same name that may be used elsewhere in the program.
- Functions can communicate information back to the caller through return values. Python functions may return multiple values. Value returning functions should generally be called from inside of an expression. Functions that don’t explicitly return a value return the special object None. 
- Python passes parameters by value. If the value being passed is a mutable object, then changes made to the object may be visible to the caller.

## Decision structures

### Exception Handling

```python
import math
def main():
    print("This program finds the real solutions to a quadratic\n")
    try:
        a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2 )
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No Real Roots")
        else:
            print("You didn’t give me the right number of coefficients.")
    except NameError:
        print("\nYou didn’t enter three numbers.")
    except TypeError:
        print("\nYour inputs were not all numbers.")
    except SyntaxError:
        print("\nYour input was not in the correct form. Missing comma?")
    except:
        print("\nSomething went wrong, sorry!")
main()
```

## Defining Classes

**Object** as an active data type that knows stuff and can do stuff. More precisely, an object consists of 

1. A collection of related information. 
2. A set of operations to manipulate that information.

The information is stored inside the object in instance variables. The operations, called **methods**, are functions that “live” inside the object. Collectively, the instance variables and methods are called the attributes of an object.

For example, to take a now familiar example, a Circle object will have instance variables such as center, which remembers the center point of the circle, and radius, which stores the length of the circle’s radius, called also parameters.

Recall that every object is said to be an instance of some class. The class of the object determines what attributes the object will have. Basically a class is a description of what its instances will know and do. New objects are created from a class by invoking a constructor. You can think of the class itself as a sort of factory for stamping out new instances.



```python
class MSDie:  # also caled constructor
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides + 1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

def main():
    die1 = MSDie(12)
    die2 = MSDie(100)
    die1.roll()
    print(die1.getValue())

main()
```

Each method definition looks like a normal function definition. Placing the function inside a class makes it a method of that class, rather than a stand-alone function.

Let’s take a look at the three methods defined in this class. You’ll notice that each method has a first parameter named **self**. The first parameter of a method is special—it always contains a reference to the object on which the method is acting. As usual, you can use any name you want for this parameter, but the traditional name is self, so that is what I will always use.

OK, so self is a parameter that represents an object. But what exactly can we do with it? The main thing to remember is that objects contain their own data. Conceptually, instance variables provide a way to remember data inside an object. Just as with regular variables, instance variables are accessed by name. We can use our familiar dot notation: .. Look at the definition of setValue; self.value refers to the instance variable value that is associated with the object. Each instance of a class has its own instance variables, so each MSDie object has its very own value.

Certain methods in a class have special meaning to Python. These methods have names that begin and end with two underscores. The special method __init__ is the object constructor. Python calls this method to initialize a new MSDie. The role of __init__ is to provide initial values for the instance variables of an object.

```python
From outside the class, the constructor is referred to by the class name.

die1 = MSDie(6)

When executing this statement, Python creates a new MSDie and executes __init__ on that object.

The net result is that die1.sides is set to 6 and die1.value is set to 1.

```

Accessing the instance variables of an object is very handy for testing purposes, but it is generally considered poor practice to do this in programs. One of the main reasons for using objects is to hide the internal complexities of those objects from the programs that use them. References to instance variables should generally remain inside the class definition with the rest of the implementation details. From outside the class, all interaction with an object should generally be done using the interface provided by its methods. However, this is not a hard and fast rule, and Python program designers often specify that certain instance variables are accessible as part of the interface.

### Summary

- An object comprises a collection of related data and a set of operations to manipulate that data. Data is stored in instance variables and manipulated via methods.
-  Every object is an instance of some class. It is the class definition that determines what the attributes of the object will be. Programmers can create new kinds of objects by writing suitable class definitions. 
- A Python class definition is a collection of function definitions. These functions implement the methods of the class. Every method definition has a special first parameter called self. The actual parameter of self is the object to which the method is being applied. The self parameter is used to access the attributes of the object via dot notation.
- The special method __init__ is the constructor for a class. Its job is to initialize the instance variables of an object.
- Defining new objects (via class) can simplify the structure of a program by allowing a single variable to store a constellation of related data. Objects are useful for modeling real world entities. These entities may have complex behavior that is captured in method algorithms (e.g., a projectile) or they may be little more than a collection of relevant information about some individual (e.g., a student record).



## Object-Oriented Design

Now that you know some data structuring techniques, it’s time to stretch your wings and really put those tools to work. Most modern computer applications are designed using a data-centered view of computing. This so-called object-oriented design (OOD) process is a powerful complement to top-down design for the development of reliable, cost-effective software systems.

A client only needs to understand the interface of a service; the details of how that service is implemented are not important. In fact, the internal details may change radically and not affect the client at all. Similarly, the component providing the service does not have to consider how the service might be used. The black box just has to make sure that the service is faithfully delivered. This separation of concerns is what makes the design of complex systems possible.

In top-down design, functions serve the role of our magical black boxes. A client program can use a function as long as it understands what the function does. The details of how the task is accomplished are encapsulated in the function definition.

In object-oriented design, the black boxes are objects. The magic behind objects lies in class definitions. Once a suitable class definition has been written, we can completely ignore how the class works and just rely on the external interface—the methods.

If we can break a large problem into a set of cooperating classes, we drastically reduce the complexity that must be considered to understand any given part of the program. Each class stands on its own. Object-oriented design is the process of finding and defining a useful set of classes for a given problem. Like all design, it is part art and part science.

Just to get you started, here are some intuitive guidelines for object-oriented design: 

1. Look for object candidates. Your goal is to define a set of objects that will be helpful in solving the problem. Start with a careful consideration of the problem statement. Objects are usually described by nouns. You might underline all of the nouns in the problem statement and consider them one by one. Which of them will actually be represented in the program? Which of them have “interesting” behavior? Things that can be represented as primitive data types (numbers or strings) are probably not important candidates for objects. Things that seem to involve a grouping of related data items (e.g., coordinates of a point or personal data about an employee) probably are. 
2. Identify instance variables. Once you have uncovered some possible objects, think about the information that each object will need to do its job. What kinds of values will the instance variables have? Some object attributes will have primitive values; others might themselves be complex types that suggest other useful objects/classes. Strive to find good “home” classes for all the data in your program. 
3. Think about interfaces. When you have identified a potential object/class and some associated data, think about what operations would be required for objects of that class to be useful. You might start by considering the verbs in the problem statement. Verbs are used to describe actions—what must be done. List the methods that the class will require. Remember that all manipulation of the object’s data should be done through the methods you provide.
4. Refine the nontrivial methods. Some methods will look like they can be accomplished with a couple of lines of code. Other methods will require considerable work to develop an algorithm. Use top-down design and stepwise refinement to flesh out the details of the more difficult methods. As you go along, you may very well discover that some new interactions with other classes are needed, and this might force you to add new methods to other classes. Sometimes you may discover a need for a brand-new kind of object that calls for the definition of another class.
5. Design iteratively. As you work through the design, you will bounce back and forth between designing new classes and adding methods to existing classes. Work on whatever seems to be demanding your attention. No one designs a program top to bottom in a linear, systematic fashion. Make progress wherever it seems progress needs to be made. 
6. Try out alternatives. Don’t be afraid to scrap an approach that doesn’t seem to be working or to follow an idea and see where it leads. Good design involves a lot of trial and error. When you look at the programs of others, you are seeing finished work, not the process they went through to get there. If a program is well designed, it probably is not the result of a first try. Fred Brooks, a legendary software engineer, coined the maxim: “Plan to throw one away.” Often you won’t really know how a system should be built until you’ve already built it the wrong way. 
7. Keep it simple. At each step in the design, try to find the simplest approach that will solve the problem at hand. Don’t design in extra complexity until it is clear that a more complex approach is needed.

Another advantage of encapsulation is that it supports code reuse. It allows us to package up general components that can be used from one program to the next. The DieView class and Button classes are good examples of reusable components. 

Encapsulation is probably the chief benefit of using objects, but alone it only makes a system object-based. To be truly objected-oriented, the approach must also have the characteristics of polymorphism and inheritance.

### Polymorphism 

Literally, the word polymorphism means “many forms.” When used in object-oriented literature, this refers to the fact that what an object does in response to a message (a method call) depends on the type or class of the object. 

Our poker program illustrated one aspect of polymorphism. The PokerApp class was used both with a TextInterface and a GraphicsInterface. There were two different forms of interface, and the PokerApp class could function quite well with either. When the PokerApp called the showDice method, for example, the TextInterface showed the dice one way and the GraphicsInterface did it another way. 

In our poker example, we used either the text interface or the graphics interface. The remarkable thing about polymorphism, however, is that a given line in a program may invoke a completely different method from one moment to the next. As a simple example, suppose you had a list of graphics objects to draw on the screen. The list might contain a mixture of Circle, Rectangle, Polygon, etc. You could draw all the items in a list with this simple code: 

```
for obj in objects: 
	obj.draw(win) 
```

Now ask yourself, what operation does this loop actually execute? When obj is a circle, it executes the draw method from the circle class. When obj is a rectangle, it is the draw method from the rectangle class, etc.

 Polymorphism gives object-oriented systems the flexibility for each object to perform an action just the way that it should be performed for that object. Before object orientation, this kind of flexibility was much harder to achieve.

### Inheritance 

The third important property for object-oriented approaches, inheritance, is one that we have not yet used. The idea behind inheritance is that a new class can be defined to borrow behavior from another class. The new class (the one doing the borrowing) is called a subclass, and the existing class (the one being borrowed from) is its superclass.

For example, if we are building a system to keep track of employees, we might have a class Employee that contains the general information that is common to all employees. One example attribute would be a homeAddress method that returns the home address of an employee. Within the class of all employees, we might distinguish between SalariedEmployee and HourlyEmployee. We could make these subclasses of Employee, so they would share methods like homeAddress. However, each subclass would have its own monthlyPay function, since pay is computed differently for these different classes of employees. 

Inheritance provides two benefits. One is that we can structure the classes of a system to avoid duplication of operations. We don’t have to write a separate homeAddress method for the HourlyEmployee and SalariedEmployee classes. A closely related benefit is that new classes can often be based on existing classes, promoting code reuse. 

We could have used inheritance to build our poker program. When we first wrote the DieView class, it did not provide a way of changing the appearance of the die. We solved this problem by modifying the original class definition. An alternative would have been to leave the original class unchanged and create a new subclass ColorDieView. A ColorDieView is just like a DieView except that it contains an additional method that allows us to change its color. Here is how it would look in Python:

```python
class ColorDieView(DieView):
	def setValue(self, value):
        self.value = value
        DieView.setValue(self, value)
    def setColor(self, color):
        self.foreground = color
        self.setValue(self.value)
```

The first line of this definition says that we are defining a new class ColorDieView that is based on (i.e., a subclass of) DieView. Inside the new class, we define two methods. The second method, setColor, adds the new operation. Of course, in order to make setColor work, we also need to modify the setValue operation slightly. 

The setValue method in ColorDieView redefines or overrides the definition of setValue that was provided in the DieView class. The setValue method in the new class first stores the value and then relies on the setValue method of the superclass DieView to actually draw the pips. Notice especially how the call to the method from the superclass is made. The normal approach self.setValue(value) would refer to the setValue method of the ColorDieView class, since self is an instance of ColorDieView. In order to call the original setValue method from the superclass, it is necessary to put the class name where the object would normally go.

```
DieView.setValue(self, value)
```

 The actual object to which the method is applied is then sent as the first parameter.

## Algorithm Design and Recursion

I said earlier that Python uses a linear search algorithm to implement its built-in searching methods. If a binary search is so much better, why doesn’t Python use it? The reason is that the binary search is less general; in order to work, the list must be in order. If you want to use binary search on an unordered list, the first thing you have to do is put it in order or sort it. This is another well-studied problem in computer science, and one that we should look at. Before we turn to sorting, however, we need to generalize the algorithm design technique that we used to develop the binary search.

### Recursion vs. Iteration

 I’m sure by now you’ve noticed that there are some similarities between iteration (looping) and recursion. In fact, recursive functions are a generalization of loops. Anything that can be done with a loop can also be done by a simple kind of recursive function. In fact, there are programming languages that use recursion exclusively. On the other hand, some things that can be done very simply using recursion are quite difficult to do with loops. 

For a number of the problems we’ve looked at so far, we have had both iterative and recursive solutions. In the case of factorial and binary search, the loop version and the recursive version do basically the same calculations, and they will have roughly the same efficiency. The looping versions are probably a bit faster because calling functions is generally slower than iterating a loop, but in a modern language the recursive algorithms are probably fast enough.

Typically, you use a recursive function to divide a big problem that’s difficult to solve into smaller problems that are easier-to-solve.

### **Recursive Definition** 

A Recursive definition is a definition that is made in terms of the smaller version of itself. Consider the following example :
$$
xn = x * x * x * x…n times
$$
Now it can be represented in terms of recursive definition as follows :
$$
xn = x*(x^n-1) for  n > 1
$$
(This is the recursive definition)

=x (for n=1) or 1 (for n=0)

### **Disadvantages of recursion** 

Recursion, along with it, also brings some of its own disadvantages. Some are :

1. It is slower as compared to iteration.
2. Logical but difficult to find the error, if any exists.
3. Requires extra storage space this is because, for every recursive call, separate memory is allocated for the variables.
4. Recursive functions often throw a Stack Overflow Exception when processing or operations are too large.



https://realpython.com/python-recursion/

