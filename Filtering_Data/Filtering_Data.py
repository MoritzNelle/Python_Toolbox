'''
READ ME:
- The module contains one function: filter_data
- No classes or methods are defined in this module
- The module imports the 're' module for regular expression operations

DESCRIPTION:
- The function 'filter_data' filters lines from an input file based on a regular expression pattern and writes the filtered lines to an output file.
- The function reads the input file line by line, checks each line against the provided pattern, and writes the line to the output file if it matches (or doesn't match, based on the include_flag).
- The function returns no value but prints the filtered lines to the console.

PARAMETERS:
- 'input_file' (str): The name of the input file to be read.
- 'output_file' (str): The name of the output file to be written.
- 'pattern' (str): The regular expression pattern to be used for filtering lines.
- 'include_flag' (bool): If True, lines that match the pattern are included in the output. If False, lines that do not match the pattern are included.

LIMITATIONS:
- The function assumes that the input file exists and can be opened for reading. If the file does not exist or cannot be opened, an error will be raised.
- The function assumes that the output file can be opened for writing. If the file cannot be opened, an error will be raised.
- The function does not handle exceptions that may occur during file operations.
- The function does not check the validity of the regular expression pattern. If the pattern is not a valid regular expression, an error will be raised.

STRUCTURES:
- The function uses a with-statement to open the input and output files.
- The function uses a for-loop to iterate over the lines in the input file.
- The function uses an if-elif construct to check each line against the pattern and decide whether to write it to the output file.

OUTPUTS:
- The function does not have a return statement.
- The function uses a print statement to print the filtered lines to the console. This is done for immediate feedback to the user.
'''


import re

def filter_data(input_file, output_file, pattern, include_flag):
    with open(input_file, 'r') as input_f:
        with open(output_file, 'w') as output_f:
            for line in input_f:
                if include_flag and re.search(pattern, line):
                    output_f.write(line)
                    print(line, end="")
                elif not include_flag and not re.search(pattern, line):
                    output_f.write(line)
                    print(line, end="")

# Test code
if __name__ == "__main__":
    filter_data("example.txt", "output.txt", input("\n\nInput regular expression: "), input("Include (True/False): ") == "True")

'''
Regular expressions, to test the code:
1.  Test case: listing all lines where a colon (":") is not immediately preceded by a word.
    Regular expression: (?<!\w):

2.  Test case: stripping all comment lines from a Python program.
    Regular expression: ^\s*#.*$

3.  Test case: listing all lines where one or both of the words "Latitude" and "Longitude" are missing.
    Regular expression: ^(?!.*\bLatitude\b)(?!.*\bLongitude\b).*$

4.  Test case: showing the section headers in an HTML-file, supposing each section header occupies one line; section headers are surrounded by tags "<h#>" and "</h#>" with "#" a number 1–6
    Regular expression: ^<h[1-6]>.*<\/h[1-6]>$
'''