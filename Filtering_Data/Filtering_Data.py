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