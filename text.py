import re 
with open("row.txt", 'rt+') as f:
    for lines in f:
        if re.search("ab*", lines):
            print(lines)