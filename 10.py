import re
def repl(match):
    return match.group(1).lower()
a = "HelloMyNameIs"
a = re.findall("[A-Z][^A-Z]*", a)
a = re.sub("([A-Z])", repl, "_".join(a))
print(a)