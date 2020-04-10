students = {}
with open("marks.txt", "rt") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) > 1:
            students[parts[0]] = tuple(map(int,parts[1:]))

f.close()

for n, m in students.items():
    print(f"{n:10}  {sum(m):3}")
