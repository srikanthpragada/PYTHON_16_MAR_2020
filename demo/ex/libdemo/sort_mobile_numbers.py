import re

f = open("mobiles.txt", "rt")

phones = set()

for line in f:
    # numbers = re.findall(r'\d+', line)
    numbers = re.split(r'\D+', line)
    for n in numbers:
        if len(n) == 10:
            phones.add(n)

for n in sorted(phones):
    print(n)
