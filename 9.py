import re
a = "HelloMyNameIs"
a = re.findall("[A-Z][^A-Z]*", a)
print(a)
print(" ".join(a))