import re

with open("row.txt", "rt+") as f:
    pattern = r"[\s.,]+"
    for line in f:
        if re.search(pattern, line):
            a = line
            a = re.sub(pattern, '/', a)
            print(a)

