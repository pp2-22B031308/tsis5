import re
with open("row.txt", 'rt+') as f:
    for lines in f:
        if(re.search("(?:[a-z]_[a-z]*)", lines)):
            print(lines)