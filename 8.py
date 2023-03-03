import re
a = "HelloMyNameIs"
f = re.findall("[A-Z][^A-Z]*", a)
print(" ".join(f))