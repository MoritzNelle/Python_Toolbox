# Overview of Python

## Table of Contents


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
b = a` a and b can now be used synonymmus.
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
- **Parallel Listing**: process of iterating over multiple lists simultaneously.
- **Slicing --> Sub-list**: When slicing is used on a list, it results in a new list that is a subset of the original list. This new list is often referred to as a sub-list.
- **Computer Program**: Computes an output from an input, and environment variables/side effects.
- **Functions versus a software program**: A function is a block of code that performs a specific task and returns a result. A software program is a collection of functions and data that work together to perform a bigger specific task.
- **File Object**: Represents a file on the file system. It is used to read from and write to files. `fileObject = open("filename", "mode")`


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

## Loops
 
### For-Loop
Iterate over a sequence of elements
```python
for i in range(5):
    print(i)  # prints 0, 1, 2, 3, 4
```

### While-Loop
Execute a block of code as long as a condition is true
```python
i = 0
while i < 5:
    print(i)  # prints 0, 1, 2, 3, 4
    i += 1
```

### Break-Statement
Exit a loop
```python
while True:
    print("Hello, World!")
    break
```

### Continue-Statement
Skip the rest of the loop and continue with the next iteration
```python
for i in range(5):
    if i == 2:
        continue
    print(i)  # prints 0, 1, 3, 4
```

### Return-Statement
Returns a value from inside a loop
```python
for i in range(99999):
    if i == 42:
        return i    # returns 42 and exits the loop before 99999 iterations
```

### Nested Loops
Loop inside another loop
```python
for i in range(3):
    for j in range(3):
        print(i, j)  # prints (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)
```

## Best Practices for Loops
- `break`, `returns`, and `continue` inside a loop
  - may increase efficiency, but can make the code harder to read
  - break and return are (allmost) always unnecessary in a `while`-loop


Discouraged (Example):
```python
while True:
    if condition:
        break
    # do something
```

Recommended(Example):
```python
while not condition:
    # do something
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

## Usecases with spesific methods

### Dictionarries
```python
# Create a new dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Access a value by its key
print(my_dict["name"])  # Outputs: Alice

# Update a value
my_dict["age"] = 26

# Add a new key-value pair
my_dict["profession"] = "Engineer"

# Remove a key-value pair
del my_dict["city"]

# Check if a key exists
if "name" in my_dict:
    print("Name is in the dictionary")

# Iterate over keys
for key in my_dict:
    print(key)

# Iterate over key-value pairs
for key, value in my_dict.items():
    print(key, value)
```

### Aliasing
```python
# Aliasing, when two variables point to the same object in memory
a = [1, 2, 3]   # a is a list with the elements 1, 2, 3
b = a           # b is now an alias for a (both point to the same list in memory)
a += [4]        # a is now [1, 2, 3, 4]
print(b)        # prints [1, 2, 3, 4], b has been updated as well
a = a + [5]     # a is now [1, 2, 3, 4, 5]
print(b)        # prints [1, 2, 3, 4], b has not been updated, as a now points to a new list in memory (aliasing is broken, due to the use of the "+"-operator)

```


### Slicing
```python
# Slicing, getting a subset of elements from a data-sequence (e.g., list, string, tuple)

# Syntax: data-sequence[start:stop:step]
    # start: the index where the slice starts (inclusive)
    # stop: the index where the slice ends (exclusive)
    # step(optional): the step size for the slice (default is 1)

myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
myList[2:5]     # returns [2, 3, 4]
myList[:5]      # returns [0, 1, 2, 3, 4]
myList[5:]      # returns [5, 6, 7, 8, 9]
myList[2:8:2]   # returns [2, 4, 6]
myList[-1]      # returns 9 (last element)
myList[-3:]     # returns [7, 8, 9] (last three elements)
myList[:-3]     # returns [0, 1, 2, 3, 4, 5, 6] (all elements except the last three)
myList[::-1]    # returns [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed list)
myList[8:3:-2]  # returns [8, 6, 4] (elements from index 8 to 3 with a step of -2)
```


### Lists
```python
#Lists are mutable, ordered collections of elements that can be accessed, changed, and iterated via indexing.

#General list
[ 10, 13, 27, 148 ]
[ ‘john’, ‘mary’, ‘fred’, ‘harry’, ‘liz’]
[‘Wageningen’, 2500, 21.8]

#Empty list
[]
[ ]

#One-element list
[ 10, ] # trailing comma is allowed, but not required


#initialize a list with a fixed number of elements
[ 0 ] * 5   # [ 0, 0, 0, 0, 0 ]
[ 0, 0, 0, 0, 0 ] # same as above

#ADD ELEMENTS TO A LIST
myList = [ 10, 20, 30 ]     #example list

myList.append( 40 )         # a is now [ 10, 20, 30, 40 ]
myList = myList + [ 40 ]    # a is now [ 10, 20, 30, 40]
myList += [ 40 ]            # a is now [ 10, 20, 30, 40]
myList = [0] + myList       # a is now [ 0, 10, 20, 30]
myList.insert( 2, 15 )      # a is now [ 10, 15, 20, 30]
myList[3:3] = [ 25 ]        # a is now [ 10, 20, 25, 30]
myList[1:2] = [15]          # a is now [ 15, 20, 25, 30]


#REMOVE ELEMENTS FROM A LIST
myList = [ 10, 20, 30, 40 ] #example list

myList[2:3] = []            # a is now [ 10, 20, 40 ]
myList.remove( 30 )         # a is now [ 10, 20, 40 ]
del myList[ 2 ]             # a is now [ 10, 20, 40 ], del() does not return the removed element
myList.pop( 2 )             # a is now [ 10, 20, 40 ], pop() returns the removed element (30)


#MISSCELLANEOUS
myList = [0,1,2,3,4,5,6,7,8,9] #example list

myList.count( 10 )          # 1 #count the number of occurrences of an element in a list
myList.index( 5 )           # 5 #find the index of the first occurrence of an element in a list
myList.reverse()            # [ 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 ] #reverse the order of elements in a list
myList.sort()               # [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ] #sort the elements in a list
myList.sort( reverse = True )# [ 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 ] #sort the elements in a list in reverse order

myList = list( "hello" )    # [ 'h', 'e', 'l', 'l', 'o' ] #convert a string to a list of characters


#"change" a tuple (tuples are immutable, so you can't actually change them, but you can convert them to a list, change the list, and convert the list back to a tuple)
myTuple = (1, 2, 3)         # (1, 2, 3) #example tuple
myList = list( myTuple )    # [ 1, 2, 3 ] #convert a tuple to a list (can be changed, unlike a tuple)
myList[1:1] = [1.5]
myTuple = tuple(myList)     # (1, 2, 3) #convert a list back to a tuple (immutable)

#Function to convert a paralell list
names = ["Io", "Europa", "Ganymede", "Callisto"]
years = [1610, 1610, 1610, 1610]
masses = [8.9319e+22, 4.8000e+22, 1.4819e+23, 1.0759e+23]

def convertParallelList(names, years, masses):
    result = [None]*len(names)
    for i in range(len(names)):
        result[i] = (names[i], years[i], masses[i])
    return result

    #returns: [('Io', 1610, 8.9319e+22),
    #          ('Europa', 1610, 4.8e+22),
    #          ('Ganymede', 1610, 1.4819e+23),
    #          ('Callisto', 1610, 1.0759e+23)]


```
### Execution limitation when calling a function
Sometimes, you may want to limit the execution of a function to a specific context or environment. This can be achieved by using a decorator that checks the execution environment before running the function. This is commonly used when:
- a test function should only run when the script is executed directly, not when it is imported as a module
- a function should only run on a specific operating system
- a function should only run in a specific environment (e.g., development, production)
Here's an example of a decorator that limits the execution of a function to a specific operating system:

```python
print("Hello, World!")
if __name__ == "__main__" 
    print("This function was executed directly.")
    # This code will only run if the script is executed directly, not if it is imported as a module.
```

### File Handling
Allows to read and write data to and from files. Python provides built-in functions for file handling, such as `open()`, `read()`, `write()`, and `close()`. Here's an example of reading/writing data from/to a txt-file:

```python
# Create a new file and write data to it
txtFile = open("data.txt", "w")
for line in range(10):
    txtFile.write(f"Line {line}\n")
txtFile.close()

# Read data from an existing file
txtFile = open("data.txt", "r")
allLines = []
for line in txtFile:
    thisLine = line.strip()
    allLines.append(thisLine)
print(allLines)
txtFile.close()
```
### Local and Global Variables
Variables in Python can be either local or global.
- **Local variables** are defined inside a function and can only be accessed within that function.
- **Global variables** are defined outside of any function and can be accessed from anywhere in the program.
Here's an example of local and global variables:

```python
theNumber = 3           # global variable

def addTheNumber(x):        # local variable:
    theNumber = 5           # - does not change the global variable
    result = x + theNumber  # - only exists within the function
    return result           # - overrides the global variable within the function

a = 2
b = addTheNumber(a)
print(b)                    # Outputs: 7
print (a + theNumber)       # Outputs: 5
```
## Own Modules
A module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended.
If a module from the user shall be imported, the module must be in the same directory as the script that imports it, or the module must be in a directory that is in the Python path.
Here's an example of creating and importing a module:

```python
# Create a new module in the File: myModule.py
def myFunction():
    return("Hello, World!")

if __name__ == "__main__":  # This code will only run if the script is executed directly, not if it is imported as a module, common practice to test the module, and to avoid running the test when the module is imported.
    print myFunction()
```

```python
# Import the module
import myModule
print (myModule.myFunction())   # Prints: "Hello, World!"
```

## Write a README-section:
A read me section consists of the following headers (should always be there and can be used as a way of structuring):
1. READ ME
1. DESCRIPTION
1. PARAMETERS
1. LIMITATIONS
1. STRUCTURES
1. OUTPUT

### exsample function
- all following examples will refere to this example:

```python
def common_chars(str1,str2):
	commons = ''
	for ch in str1:
		if ch in str2:
			if ch not in commons:
				commons += str(ch)
	return commons
```

### READ ME:
- The subsection READ ME should be a list of:
  - Functions in the module
  - Classes and methods
  - Methods and functions that were imported (and their module)
- Example:
```python
"common_chars function"
```


### DESCRIPTION:
- What does the function do?
- How is relevant information/data obtained?
- What is the output/return value of the function?
#### Example:
```python
"common_chars is a function that compares two textual inputs, supplied through parameters,and returns a string of common  characters found in both inputs."
```


### PARAMETERS:
- Which parameters the function takes (and their data type)
- How parameters are used by the function
#### Example:
```python
"str1 - a string value, which should be compared to str2
str2 - a string value, which should be compared to str1"
```


### LIMITATIONS:
Supply at least two limitations of the function(s):
- Type based limitations
- Efficiency based limitations
- Potential errors for specific cases
- Other limitations?
- real world limitations

#### Example:
```python
"- Not exclusively applicable to strings, will work with any iterable, even with some mixed combinations of types
- Compares all characters, even if a character has already found to be common between str1 and str2
- If an iteration for str1 contains a non-str type and str2 is of type str, an error will be raised."
```

### STRUCTURES:
should inform on the implementation and functionality on any of the following structures and functions:
- If-elif-else constructs
- For-loops
- While-loops
- Use of the function input

#### Example:
```python
" A for-loop was applied to go through each character of the input str1 (or indeed each element of any iterable supplied to str1)
- An if-statement to check whether the character currently in variable ch from the for-loop is present in str2
- An if-statement to check whether a character is already in the list of common characters"
```


#### OUTPUTS:
should inform on any outputs:
- Return-statements
- Print-statements (and why it was chosen to use a print-statement)