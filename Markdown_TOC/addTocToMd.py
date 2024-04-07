def generate_toc(file_path):
    """
    Generates a table of contents (TOC) for a Markdown file.

    Args:
        file_path (str): The path to the Markdown file.
    Returns:
        str: The generated table of contents.
    
    - Can handle up to 6 levels of headings.
    - Ignores '#' characters in code blocks.
    - Adds an anchor to each heading.    
    """
    mdFile = open(file_path, 'r')

    toc_lines = []
    headings = []
    codeBlock = False

    for line in mdFile:

        if line.startswith("```python"):
            codeBlock = True
        elif line.startswith("```"):
            codeBlock = False

        if line.startswith('#') and not codeBlock:
            level = line.count('#')
            heading = line.strip('#').strip().strip(':')
            anchor = heading.lower().replace(' ', '-')
            toc_line = '  ' * (level - 1) + f'- [{heading}](#{anchor})\n'
            toc_lines.append(toc_line)
            headings.append((level, heading, anchor))

    toc = ''.join(toc_lines)

    for level, heading, anchor in headings:
        toc += f'<a name="{anchor}"></a>\n'

    mdFile.close()
    return toc


def writeToc(toc, filePath):
    """
    Writes the table of contents (toc) to a Markdown file at the specified file path.

    Args:
        toc (list): The table of contents to be written.
        filePath (str): The file path of the Markdown file.

    Returns:
        None
    """
    mdFile = open(filePath, 'r+')
    mdFileCopy = mdFile.readlines()

    for i in range(len(mdFileCopy)):
        if "Table of Contents" in mdFileCopy[i]:
            mdFileCopy[i+1:i+1] = toc

    mdFileCopy = ''.join(mdFileCopy)
    
    mdFile.seek(0)
    mdFile.write(mdFileCopy)
    mdFile.truncate()
    mdFile.close()
    print("Table of contents added successfully.")
            
if __name__ == "__main__":
    filePath = input("Enter the file path: ")
    toc = generate_toc(filePath)
    writeToc(toc, filePath)