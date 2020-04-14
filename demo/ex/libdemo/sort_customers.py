import re

f = open("customers.txt", "rt")

custs = {}

for line in f:
    # get name
    name = re.search('[a-zA-Z ]+', line)
    if name is None:  # Name not found
        continue

    # get mobile
    mobile = re.search(r"\d+", line)
    if mobile is None:  # Mobile not found
        continue

    custs[name.group(0).strip()] = mobile.group(0)

for n, m in sorted(custs.items()):
    print(f"{n:20} {m}")
