import os


def print_file(filename):
    lineno = 1
    with open(filename) as f:
        for line in f:
            print(f"{lineno:03}: {line}", end='')
            lineno += 1


for (dname, dirs, files) in os.walk(r"c:\classroom\mar16\demo"):
    for filename in files:
        if filename.endswith('.py'):
            fullpath = dname + "\\" + filename
            print("\n" + fullpath)
            print("=" * len(fullpath))
            print_file(fullpath)
