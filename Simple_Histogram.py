'''
READ ME:
This module provides the following functions:
- `random_numbers()`: Generates a list of 100 random numbers between 1 and 10.
- `get_frequencies(numbers)`: Calculates the frequency of each number in a list.
- `print_histogram(numbers)`: Prints a histogram based on the frequency of numbers.

DESCRIPTION:
This module is a simple histogram generator. It generates a list of 100 random numbers between 1 and 10, calculates the frequency of each number, and prints a histogram where each bar represents the frequency of a number.

PARAMETERS:
- `numbers`: a list of integers. This list is used as the input for both `get_frequencies` and `print_histogram` functions.

LIMITATIONS:
- The functions do not handle non-integer inputs. If the list contains non-integer elements, an error will be raised.
- The functions do not handle empty lists. If an empty list is passed, `print_histogram` will not print anything.
- The range of random numbers generated by `random_numbers` is hardcoded and cannot be changed without modifying the function.

STRUCTURES:
- The `random_numbers` function uses a for-loop to generate the list of random numbers.
- The `get_frequencies` function uses a for-loop to iterate over the list of numbers and a dictionary to store the frequencies.
- The `print_histogram` function uses the `get_frequencies` function to get the frequencies, a for-loop to iterate over the sorted frequencies, and a print statement to print each bar of the histogram.

OUTPUTS:
- The `random_numbers` function returns a list of 100 random numbers.
- The `get_frequencies` function returns a dictionary where the keys are the numbers and the values are their frequencies.
- The `print_histogram` function prints the histogram to the console. Each line of the histogram represents a number and its frequency.
'''

import random

def random_numbers():
    numbers = []
    for _ in range(100):
        number = random.randint(1, 10)
        numbers.append(number)
    return numbers

def get_frequencies(numbers):
    frequencies = {}
    for number in numbers:
        frequencies[number] = frequencies.get(number, 0) + 1
    return frequencies

def print_histogram(numbers):
    frequencies = get_frequencies(numbers)
    for number, frequency in sorted(frequencies.items()):
        print(f"{number} {'#' * frequency}")

# Example usage
print_histogram(random_numbers())