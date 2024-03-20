#list of functions used in PIP

'''
Python-FUNCTIONS:
- float:        converts a string or a number to a floating point number, e.g., float("3.14") returns 3.14
- int:          converts a string or a number to an integer, e.g., int("3.14") returns 3
- in:           checks if a value is in a list, e.g., 3 in [1, 2, 3] returns True
- print:        prints a value to the console  e.g., print("Hello, World!") prints "Hello, World!"; print(3.14) prints 3.14; print(list) prints [1, 2, 3]
- exit:         exits the program and returns to the command line
- append:       adds an element to the end of a list, e.g., list.append(4) adds 4 to the end of list
- len:          returns the length of a list, e.g., len([1, 2, 3]) returns 3
- return:       returns a value from a function, e.g., return three returns 3
- input:        gets input from the user, e.g., input("Enter a number: ") gets a number from the user, int(input("Enter a number: ")) gets an integer from the user
- split:        splits a string into a list of strings, e.g., "1 2 3".split() returns ["1", "2", "3"]; "1,2,3".split(",") returns ["1", "2", "3"]
- str.isdigit:  checks if a string is a number, e.g., "123".isdigit() returns True; while "abc".isdigit() returns False
- str.find:     finds the index of a substring in a string, e.g., "Hello, World!".find("World") returns 7; if the substring is not found, it returns -1 (compare with str.index)
- str.index:    finds the index of a substring in a string, e.g., "Hello, World!".index("World") returns 7; if the substring is not found, it raises a ValueError (compare with str.find)
- str.upper:    converts a string to uppercase, e.g., "hello".upper() returns "HELLO"
- str.slice:    returns a slice of a list, e.g., list[1:3] returns [2, 3]; list[:3] returns [1, 2, 3]; list[3:] returns [4, 5, 6]
- str.join:     joins a list of strings with a string, e.g., ", ".join(["apple", "banana", "cherry"]) returns "apple, banana, cherry"
- str.strip:    removes leading and trailing whitespace from a string, e.g., "  Hello, World!  ".strip() returns "Hello, World!"
- str.split:    splits a string into a list of strings, e.g., "1 2 3".split() returns ["1", "2", "3"]; "1,2,3".split(",") returns ["1", "2", "3"]
- str.replace:  replaces a substring with another substring in a string, e.g., "Hello, World!".replace("World", "Python") returns "Hello, Python!"
- str.isdigit:  checks if a string is a number, e.g., "123".isdigit() returns True
- * :           tuple unpacking e.g., distance(*input2haversine(inputStringA, inputStringB))
- 

MODULES:
- math: provides mathematical functions, e.g., math.sqrt(4) returns 2, math.pi returns 3.141592653589793, math.sin(math.pi/2) returns 1.0
- 

OPERATORS:
- + :   addition, string concatenation, list concatenation
- - :   subtraction, negation, list difference
- * :   multiplication, repetition, list repetition
- / :   division
- // :  floor division
- % :   modulus, string formatting
- ** :  exponentiation
- < :   less than
- <= :  less than or equal to
- > :   greater than
- >= :  greater than or equal to
- == :  equal to
- != :  not equal to
- and : logical and
- or :  logical or
- not : logical not
- += :  addition assignment
- -= :  subtraction assignment
- 


STRUCTURE:
- if:       conditional statement that executes a block of code if a condition is true
-- elif:    conditional statement that executes a block of code if the previous if-condition is false and the current condition is true
-- else:    conditional statement that executes a block of code if the previous if-condition is false

- for:      loop that iterates over a sequence of elements, usualy used for count bound loop; e.g., for i in range(5): print(i) prints 0, 1, 2, 3, 4
- while:    loop that executes a block of code as long as a condition is true, usualy used for sentinel- or data-bound-loop; e.g., while i < 5: print(i); i += 1 prints 0, 1, 2, 3, 4
- break:    statement that exits a loop; e.g., while True: print("Hello, World!"); break prints "Hello, World!"
- continue: 


Python-DEFINITIONS:
- function heading ("def"): first line of a function definition, contains the keyword "def", the function name, the parameter list, and a colon
- function body:            block of statements that define the function
- procedure:                function that does not return a value
- parameter:                variable that receives an argument value
- argument:                 value that is passed to a function
- control structure:        block of code that controls the flow of a program e.g., if, for, while
- controlled code:          the block of code that is controlled by a control structure e.g., the block of code that is executed if an if statement is true
- function call:            statement that executes a function and hands over arguments
- functional programming:   programming paradigm that uses functions as the primary building blocks of a program
- bulk testing:             testing with a large number of test cases, inputed  by the user
- edge case:                a test case that is at the boundary of what is expected, e.g., a triangle with all sides of length 0; a tringle with a + b = c (a line)
- debugging:                the process of FINDING and FIXING errors in a program

Python-DATATYPES:
- int:       integer number, e.g., 42
- float:     floating point number, e.g., 3.14
- str:       string, e.g., "Hello, World!"
- list:      ordered collection of elements that can be changed via indexing, e.g., [1, 2, 3] (compare with tuple)
- tuple:     ordered collection of elements that cannot be changed after creation, e.g., (1, 2, 3) (compare with list)
- bool:      boolean value aquired by a logical operation, e.g. 1 == 1 returns True, 1 == 2 returns False
- NONE:      special constant that represents the absence of a value or a null value. It is an object of its own datatype, the NoneType
- NULL:      

'''