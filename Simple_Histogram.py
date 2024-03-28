'''
READ ME:
- random_numbers function
- get_frequencies function
- print_histogram function
- random module

DESCRIPTION:
- The Simple_Histogram.py program generates a list of 100 random numbers between 1 and 20, calculates the frequency of each number, and prints a histogram of the frequencies.
- The random_numbers function generates the list of random numbers.
- The get_frequencies function calculates the frequency of each number in the list.
- The print_histogram function prints the histogram.

PARAMETERS:
- The random_numbers function does not take any parameters.
- The get_frequencies function takes a list of numbers as a parameter.
- The print_histogram function takes a list of numbers as a parameter.

LIMITATIONS:
- The program only works with integers between 1 and 20.
- The program does not handle non-integer or out-of-range inputs.
- The program does not provide any way to customize the range of numbers or the number of numbers generated.

STRUCTURES:
- The random_numbers function uses a for-loop to generate the list of random numbers.
- The get_frequencies function uses a for-loop and a dictionary to calculate the frequencies.
- The print_histogram function uses a for-loop, the min and max functions, and the range function to print the histogram.

OUTPUTS:
- The random_numbers function returns a list of random numbers.
- The get_frequencies function returns a dictionary of number frequencies.
- The print_histogram function does not return anything; it prints the histogram directly.
'''


import random

def random_numbers():
    numbers = []
    for _ in range(100):                # The underscore is used to indicate that the loop variable is not used in the loop body.
        number = random.randint(1, 20)
        numbers.append(number)
    return numbers

def get_frequencies(numbers):
    frequencies = {}
    for number in numbers:
        frequencies[number] = frequencies.get(number, 0) + 1
    return frequencies

def print_histogram(numbers):
    frequencies = get_frequencies(numbers)
    min_number = min(numbers)
    max_number = max(numbers)
    for number in range(min_number, max_number + 1):    # The range function generates a sequence of numbers from min_number to max_number.
        frequency = frequencies.get(number, 0)
        print(f"{number} {'#' * frequency}")

# Example usage
print_histogram(random_numbers())