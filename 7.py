import re
a = "It_is_snake_case"

def repl(match):
    return match.group(1) + match.group(2).upper()

a = re.sub("(.?)_([a-z])", repl, a)
print(a)