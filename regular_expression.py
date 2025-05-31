import re

name = "Bob Jerry"

if matches := re.search(r"^(\w+)[, ]?(\w+)$", name, re.IGNORECASE):
    print(matches.groups())
else:
    print("Invalid")