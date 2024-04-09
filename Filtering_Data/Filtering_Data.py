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