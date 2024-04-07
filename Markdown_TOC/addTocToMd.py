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
    #mdFileCopy = detectToc(mdFileCopy)

    for i in range(len(mdFileCopy)):
        if "Table of Contents" in mdFileCopy[i] and "- [" not in mdFileCopy[i+1]:
            mdFileCopy[i+1:i+1] = toc
            mdFileCopy = ''.join(mdFileCopy)
            
            mdFile.seek(0)
            mdFile.write(mdFileCopy)
            mdFile.truncate()
            mdFile.close()
            print("Table of contents added successfully.")
            break
        
        elif "Table of Contents" in mdFileCopy[i] and "- [" in mdFileCopy[i+1]:
            print ("Table of contents already present. Please remove the existing TOC and try again.")
            break

        elif i == len(mdFileCopy)-1:
            print("Table of contents not added. Please add a 'Table of Contents' heading in the markdown file.")
            break


'''
def detectToc(mdFileCopy):
    toc_start = None
    toc_end = None

    for i in range(len(mdFileCopy)):
        if "Table of Contents" in mdFileCopy[i] and ("- [" in mdFileCopy[i+1] or "<a name" in mdFileCopy[i+1]):
            toc_start = i
            for j in range(i, len(mdFileCopy)):
                if "- [" not in mdFileCopy[j] and "<a name" not in mdFileCopy[j]:
                    toc_end = j
                    break
        
    if toc_start is not None and toc_end is not None:
        del mdFileCopy[toc_start:toc_end+1]
        print("Old TOC detected and deleted successfully.")
    else:
        print("No old TOC found.")

    return mdFileCopy
'''
            
if __name__ == "__main__":
    filePath = input("Enter the file path: ")
    toc = generate_toc(filePath)
    writeToc(toc, filePath)