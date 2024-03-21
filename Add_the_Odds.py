'''
READ ME:
The module contains the function addTheOdds.
No classes, methods, or imported functions are used in this module.

DESCRIPTION:
addTheOdds is a function that takes a list of numbers as input and returns the sum of all odd numbers in the list.
The function iterates over the input list, checking each number to see if it is odd. If it is, it adds it to the sum.
The function returns the sum of all odd numbers in the list.

PARAMETERS:
list - a list of numbers. The function iterates over this list to find and sum all odd numbers.

LIMITATIONS:
The function assumes that the input list contains only numbers. If the list contains non-numeric elements, the function may raise an error.
The function does not handle cases where the input list contains None or NaN values.
The function uses a simple linear search to find the odd numbers, which may not be efficient for large lists.

STRUCTURES:
A for-loop is used to iterate over each number in the input list.
An if-statement is used inside the for-loop to check if the current number is odd, and if it is, it is added to the sum.

OUTPUTS:
The function returns the sum of all odd numbers in the list. A print-statement is used in the main body of the script (outside the function) to print the result of the function when it is called with a specific list.
'''

def addTheOdds(list):
    sum = 0
    for num in list:
        if num % 2 != 0:        # Check if the number is odd, i.e. if the remainder (%-operator) is not 0
            sum = sum + num     # Add the odd number to the sum
    return sum

print(addTheOdds([3,5,8,1,-1,39,20]))