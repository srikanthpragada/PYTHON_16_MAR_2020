# Display factors for the given number
import sys

if len(sys.argv) < 2:
    print("Usage : python factors.py number")
    sys.exit(1)   # Exit program

num = int(sys.argv[1])
for i in range(2, num//2 + 1):
    if num % i == 0:
        print(i)

