import re
with open("row.txt", 'rt+') as f:
    for lines in f:
        if(re.search("(a.+b$)", lines)):
            print(lines)