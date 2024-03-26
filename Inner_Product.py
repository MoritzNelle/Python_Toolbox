'''
## READ ME:
- The module `Inner_Product.py` contains the function `inprod`.
- No classes, methods, or imported functions are used in this module.

## DESCRIPTION:
- The `inprod` function calculates the inner product (also known as the dot product) of two vectors.
- The vectors are supplied as parameters to the function.
- The function returns the calculated inner product as an integer or float.

## PARAMETERS:
- `a` - a list of numbers (integers or floats), representing the first vector.
- `b` - a list of numbers (integers or floats), representing the second vector.
- The function multiplies corresponding elements from `a` and `b` and sums the results.

## LIMITATIONS:
- The function only works with lists of numbers. Other data types will raise an error.
- The function requires that the two input lists have the same length. If they don't, a `ValueError` is raised.
- The function does not handle complex numbers.

## STRUCTURES:
- An if-statement is used to check if the lengths of the input lists are equal.
- A for-loop is used to iterate over the elements of the input lists.
- The function input is used in the for-loop and the if-statement.

## OUTPUT:
- The function returns the calculated inner product.
- There are no print-statements in the function. The result is returned so that it can be used in further calculations if needed.
'''

def inprod(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")
    
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    
    return result

a = [3, -2, 0,  1]
b = [3,  4, 2, -5]

print(inprod(a, b))