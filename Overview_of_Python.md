# Overview of Python
## Python Functions

- `float`: converts a string or a number to a floating point number, e.g., `float("3")` returns `3.0`
- `int`: converts a string or a number to an integer, e.g., `int("3.14")` returns `3`
- `in`: checks if a value is in a list, e.g., `3 in [1, 2, 3]` returns `True`
- `print`: prints a value to the console, e.g., `print("Hello, World!")` prints "Hello, World!"
- `exit`: exits the program and returns to the command line
- `append`: adds an element to the end of a list, e.g., `list.append(4)` adds `4` to the end of `list`
- `len`: returns the length of a list, e.g., `len([1, 2, 3])` returns `3`
- `return`: returns a value from a function, e.g., `return three` returns `3`
- `input`: gets input from the user, e.g., `input("Enter a number: ")` gets a number from the user
- `split`: splits a string into a list of strings, e.g., `"1 2 3".split()` returns `["1", "2", "3"]`
- `str.isdigit`: checks if a string is a number, e.g., `"123".isdigit()` returns `True`
- `str.find`: finds the index of a substring in a string, e.g., `"Hello, World!".find("World")` returns `7`
- `str.index`: finds the index of a substring in a string, e.g., `"Hello, World!".index("World")` returns `7`
- `str.upper`: converts a string to uppercase, e.g., `"hello".upper()` returns `"HELLO"`
- `str.slice`: returns a slice of a list, e.g., `list[1:3]` returns `[2, 3]`
- `str.join`: joins a list of strings with a string, e.g., `", ".join(["apple", "banana", "cherry"])` returns `"apple, banana, cherry"`
- `str.strip`: removes leading and trailing whitespace from a string, e.g., `"  Hello, World!  ".strip()` returns `"Hello, World!"`
- `str.split`: splits a string into a list of strings, e.g., `"1 2 3".split()` returns `["1", "2", "3"]`
- `str.replace`: replaces a substring with another substring in a string, e.g., `"Hello, World!".replace("World", "Python")` returns `"Hello, Python!"`

### Examples:
```python
print(float("3"))  # returns 3.0
print(int("3.14"))  # returns 3
print(3 in [1, 2, 3])  # returns True
print("Hello, World!")  # prints "Hello, World!"
# exit()  # exits the program and returns to the command line
my_list = [1, 2, 3]
my_list.append(4)  # adds 4 to the end of my_list
print(len(my_list))  # returns 4
# return three  # returns 3 (only valid inside a function)
# input("Enter a number: ")  # gets a number from the user
print("1 2 3".split())  # returns ["1", "2", "3"]
print("123".isdigit())  # returns True
print("Hello, World!".find("World"))  # returns 7
print("Hello, World!".index("World"))  # returns 7
print("hello".upper())  # returns "HELLO"
print(my_list[1:3])  # returns [2, 3]
print(", ".join(["apple", "banana", "cherry"]))  # returns "apple, banana, cherry"
print("  Hello, World!  ".strip())  # returns "Hello, World!"
print("Hello, World!".replace("World", "Python"))  # returns "Hello, Python!"
```

## Python Modules

- `math`: provides mathematical functions, e.g., `math.sqrt(4)` returns `2`, `math.pi` returns `3.141592653589793`, `math.sin(math.pi/2)` returns `1.0`
- `random`: provides various functions for generating random numbers. This module uses the pseudo-random number generator function `random()`, which generates a random float number between 0.0 and 1.0. e.g, `random()`: Returns a random float number between 0.0 and 1.0.

### Examples:
```python
import math
print(math.sqrt(4))         # returns 2
print(math.pi)              # returns 3.141592653589793
print(math.sin(math.pi/2))  # returns 1.0

import random
print(random.random())                  # Generate a random float number between 0.0 and 1.0
print(random.randint(1, 10))            # Generate a random integer between 1 and 10
print(random.choice([1, 2, 3, 4, 5]))   # Choose a random element from a list
random.shuffle([1, 2, 3, 4, 5])         # Shuffle a list

```

## Python Operators

- `+`: addition, string concatenation, list concatenation
- `-`: subtraction, negation, list difference
- `*`: multiplication, repetition, list repetition
- `/`: division
- `//`: floor division
- `%`: modulus, string formatting
- `**`: exponentiation
- `<`: less than
- `<=`: less than or equal to
- `>`: greater than
- `>=`: greater than or equal to
- `==`: equal to
- `!=`: not equal to
- `and`: logical and
- `or`: logical or
- `not`: logical not
- `+=`: addition assignment
- `-=`: subtraction assignment

### Examples:
```python
# Python Operators
print(1 + 2)  # returns 3
print(2 - 1)  # returns 1
print(2 * 3)  # returns 6
print(6 / 2)  # returns 3.0
print(7 // 2)  # returns 3
print(7 % 2)  # returns 1
print(2 ** 3)  # returns 8
print(1 < 2)  # returns True
print(1 <= 1)  # returns True
print(2 > 1)  # returns True
print(2 >= 2)  # returns True
print(1 == 1)  # returns True
print(1 != 2)  # returns True
print(True and False)  # returns False
print(True or False)  # returns True
print(not True)  # returns False
x = 1
x += 2  # x is now 3
print(x)
x -= 1  # x is now 2
print(x)
```

## Python Control Structures

- `if`: conditional statement that executes a block of code if a condition is true
- `elif`: conditional statement that executes a block of code if the previous if-condition is false and the current condition is true
- `else`: conditional statement that executes a block of code if the previous if-condition is false

- `for`: loop that iterates over a sequence of elements, e.g., `for i in range(5): print(i)` prints `0, 1, 2, 3, 4`
- `while`: loop that executes a block of code as long as a condition is true, e.g., `while i < 5: print(i); i += 1` prints `0, 1, 2, 3, 4`
- `break`: statement that exits a loop, e.g., `while True: print("Hello, World!"); break` prints "Hello, World!"

### Examples:
```python
# control structure: IF-STATEMENT
if 1 < 2:
    print("1 is less than 2")
elif 1 > 2:
    print("1 is greater than 2")
else:
    print("1 is equal to 2")

# control structure: FOR-LOOP
for i in range(5):
    print(i)  # prints 0, 1, 2, 3, 4

# control structure: WHILE-LOOP
i = 0
while i < 5:
    print(i)  # prints 0, 1, 2, 3, 4
    i += 1
```


## Python Definitions

- **Function heading (`def functionName (agument1, argument2):`)**: first line of a function definition, contains the keyword "def", the function name, the parameter list, and a colon
- **Function body**: block of statements that define the function
- **Procedure**: function that does not return a value
- **Parameter**: variable that receives an argument value
- **Argument**: value that is passed to a function
- **Control structure**: block of code that controls the flow of a program, e.g., if, for, while
- **Controlled code**: the block of code that is controlled by a control structure, e.g., the block of code that is executed if an if statement is true
- **Function call**: statement that executes a function and hands over arguments
- **Functional programming**: programming paradigm that uses functions as the primary building blocks of a program
- **Bulk testing**: testing with a large number of test cases, inputted by the user
- **Edge case**: a test case that is at the boundary of what is expected, e.g., a triangle with all sides of length 0; a triangle with a + b = c (a line)
- **Debugging**: the process of finding and fixing errors in a program
- **Matrix**: represented as a nested list, with each sub-list representing a row and the elements of the sub-lists representing the columns. For example, matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] represents a 3x3 matrix. Python does not have a built-in type for matrices, but they can be handled using nested lists, or using third-party libraries like NumPy.
- **Aliasing**: multiple variable names point to the same object in memory. When an object is aliased, changes made with one variable name will affect the other. E.g. `a = list(range(10));
b = a` a nd b can now be used synonymmus.
- **clone a list**: creating a new list that contains all the elements of the original list. Can be done by using the slicing operator: `a = [1,2,3];b = a[:]`.
- **Hash Table**: also known as a dictionary or associative array, is a data structure that implements an associative array abstract data type, a structure that can map keys to values.
- **Editor**: software application for creating and modifying code. Examples include Visual Studio Code, Sublime Text, PyCharm and Atom. Most editor also offer the ability to run the code from the edior --> IDE
- **IDE**: "Integrated Development Environment" is a software application that provides comprehensive facilities to programmers for software development. It normally consists of at least a source code editor, the ability to run the code, build automation tools, and a debugger.
- **Terminal**: A terminal (also known as a console or command line) is a text-based interface that can be used to input commands directly to a computer system or programming language.
- **Structured Type**: Structured types are data types that are composed of simpler data types, which are known as primitives. Examples in Python include `lists`, `tuples`, and `dictionaries`.
- **Classes**: In object-oriented programming, a class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).
- **Object-Oriented Programming**: OOP is a programming paradigm that relies on the concept of `classes` and `objects`. It is used to structure a software program into simple, reusable pieces of code blueprints (classes), which are used to create individual instances of objects.
- **Indexing**: accessing individual elements of a sequence data type (like `strings`, `lists`, and `tuples`) using their position number, which starts from 0.
- **Slicing**: getting a subset of elements from a sequence data type (like `strings`, `lists`, and `tuples`) by specifying a range of indices.
- **Methods**: functions that are associated with a particular class. They define the behaviors that an instance of the class can perform with its data.
- **Parallel Listing**: process of iterating over multiple lists simultaneously. This is typically achieved using the `zip()` function, which pairs the corresponding elements from multiple lists together.
- **Slicing --> Sub-list**: When slicing is used on a list, it results in a new list that is a subset of the original list. This new list is often referred to as a sub-list.

### Example:
```python
#short example of methods in Python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

my_circle = Circle(5)
print(my_circle.area())  # Outputs: 78.5
```


## Python Data Types

- `int`: integer number, e.g., `42`
- `float`: floating point number, e.g., `3.14`
- `str`: string, e.g., "Hello, World!"
- `list`: ordered collection of elements that can be changed via indexing, e.g., `[1, 2, 3]`
- `tuple`: ordered collection of elements that cannot be changed after creation, e.g., `(1, 2, 3)`
- `bool`: boolean value acquired by a logical operation, e.g., `1 == 1` returns `True`
- `None`: special constant that represents the absence of a value or a null value. It is an object of its own datatype, the NoneType

### Examples:
```python
print(type(42))                 # returns <class 'int'>
print(type(3.14))               # returns <class 'float'>
print(type("Hello, World!"))    # returns <class 'str'>
print(type([1, 2, 3]))          # returns <class 'list'>
print(type((1, 2, 3)))          # returns <class 'tuple'>
print(type(1 == 1))             # returns <class 'bool'>
print(type(None))               # returns <class 'NoneType'>
```


## Errors:
**SyntaxError**: This error occurs when Python encounters something that it doesn't understand. This could be due to a typo, incorrect indentation, or forgetting to close a bracket or quote.

**IndentationError**: Python uses indentation to determine the grouping of statements. Incorrect indentation will lead to this error.

**NameError**: This error occurs when Python encounters a variable that has not been defined.

**TypeError**: This error occurs when an operation or function is applied to an object of an inappropriate type.

**ValueError**: This error occurs when a function receives an argument of the correct type but an inappropriate value.

**ZeroDivisionError**: This error occurs when the second operator in the division is zero.

**ImportError**: This error occurs when an import statement fails to find the module definition or when a `from ... import` fails to find a name that is to be imported.

**AttributeError**: This error occurs when attribute reference or assignment fails.

**KeyError**: This error occurs when a dictionary is accessed with a key that does not exist in the dictionary.

**IndexError**: This error occurs when a sequence subscript is out of range.

```python
print("Hello, World!)
#This will raise a SyntaxError because the closing quote is missing

def hello():
print("Hello, World!")
#This will raise an IndentationError because the print statement is not indented correctly.

print(x)
#This will raise a NameError if `x` has not been defined.
   
"2" + 2
#This will raise a TypeError because you can't add a string to an integer.

int("Hello, World!")
# This will raise a ValueError because "Hello, World!" is not a valid integer.

1 / 0
# This will raise a ZeroDivisionError because division by zero is undefined.

import non_existent_module
# This will raise an ImportError because `non_existent_module` does not exist.

"Hello, World!".non_existent_method()
#This will raise an AttributeError because the `non_existent_method` does not exist for strings.

my_dict = {"name": "John"}
print(my_dict["age"])
# This will raise a KeyError because "age" is not a key in the dictionary.

my_list = [1, 2, 3]
print(my_list[3])
# This will raise an IndexError because the index 3 is out of range for the list.
```

