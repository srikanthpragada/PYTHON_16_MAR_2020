
nums = [10, 11, 25, 30, 50]

for n in nums:
    if n % 2 == 0:
        print(n)

for n in filter(lambda n : n % 2 == 0, nums):
    print(n)


for c in filter(str.isupper, "How Are You"):
    print(c)
