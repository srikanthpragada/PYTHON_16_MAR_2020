# Display factors for the given number
import sys

nums = list(map(int, sys.argv[1:]))
minvalue = min(nums)

factors = []
for i in range(2, minvalue // 2 + 1):
    for n in nums:
        if n % i != 0:
            break
    else:
        factors.append(i)

print("Common Factors : ", factors)
