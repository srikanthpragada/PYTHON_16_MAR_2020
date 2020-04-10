f = open("names.txt", "rt")

names = []
for line in f.readlines():
    for name in line.split(","):
        names.append(name.strip())

f.close()

for name in sorted(names):
    print(name)
