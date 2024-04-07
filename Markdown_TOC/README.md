# Table of Contents (TOC) Generator

## Overview

The TOC Generator is a Python script that automatically generates a Table of Contents for a Markdown file. It scans the file for headings and creates a list of links to these headings, which can be used for easy navigation within the document.

## How It Works

The script works in two main steps: generating the TOC and writing it to the file:

### 1. Generating the TOC

The [`generate_toc`](command:_github.copilot.openSymbolInFile?%5B%22Python_Toolbox_(GitHub)%2FMarkdown_TOC%2FaddTocToMd.py%22%2C%22generate_toc%22%5D "Python_Toolbox_(GitHub)/Markdown_TOC/addTocToMd.py") function opens the specified Markdown file and reads it line by line. It keeps track of whether it's currently inside a code block to avoid treating code comments as headings.

For each line that starts with a '#' character (indicating a heading) and is not inside a code block, it determines the level of the heading based on the number of '#' characters. It then creates a string representing a TOC line for this heading, which includes the heading text and a link to an anchor with the same name.

These TOC lines are collected into a list, which is then joined into a single string to form the TOC.

### 2. Writing the TOC to the File
The [`writeToc`](command:_github.copilot.openSymbolInFile?%5B%22Python_Toolbox_(GitHub)%2FMarkdown_TOC%2FaddTocToMd.py%22%2C%22writeToc%22%5D "Python_Toolbox_(GitHub)/Markdown_TOC/addTocToMd.py") function opens the specified Markdown file in read-write mode and reads all its lines into a list. It then looks for the line containing the text "Table of Contents" and inserts the generated TOC immediately after this line.

The modified lines are then joined into a single string, which is written back to the file, replacing its original content.

## How to Interact with the Software

To use the TOC Generator, you need to run the script and provide the path to the Markdown file as input when prompted:

```sh
python addTocToMd.py
```

When you see the prompt "Enter the file path:", enter the path to your Markdown file. The script will then generate the TOC and write it to the file.


## Conditions for the TOC Generator

The TOC Generator is designed to work under the following conditions:

1. **Markdown File**: The input file should be a Markdown file. The program identifies headings based on the Markdown syntax (lines starting with '#').

1. **Python Environment**: The script is written in Python and requires a Python environment to run. It has been tested with Python 3.7 and above.

1. **"Table of Contents" Header**: The script looks for a line containing the text "Table of Contents" to determine where to insert the generated TOC. If this line is not found, the script will not modify the file.

1. **File Permissions**: The script needs to have read and write permissions for the file. If the file is read-only or the script does not have the necessary permissions, it will not be able to modify the file.

2. **Single Line Headings**: The script assumes that each heading is on a single line. If a heading spans multiple lines, it will not be correctly identified and included in the TOC.

3. **No Nested Code Blocks**: The script assumes that there are no nested code blocks in the Markdown file. If there are nested code blocks, the script may not correctly identify whether it's currently inside a code block, which could lead to incorrect TOC generation.

Please ensure these conditions are met for the TOC Generator to work as expected.