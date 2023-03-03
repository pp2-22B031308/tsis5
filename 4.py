import re

with open("row.txt", 'rt+') as f:
    for lines in f:
        if (re.search("([A-Z][a-z])", lines)):
            print(lines)
