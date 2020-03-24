div4 = set()

for i in range(1, 101):
    if i % 4 == 0:
        div4.add(i)

div5 = set()
for i in range(1, 101):
    if i % 5 == 0:
        div5.add(i)

for n in sorted(div4 & div5):
    print(n)

for n in sorted(div4 ^ div5):
    print(n)