def abs(n):
    return n if n >= 0 else -n


nums = [-10, 10, 20, -5, -7, 25]

for n in sorted(nums, key=abs):
    print(n)

for n in sorted(nums, key=lambda n: n if n >= 0 else -n):
        print(n)

names = ["A", "B", "a", "d", "X", "e"]

for n in sorted(names, key=str.upper):
    print(n)

names = ["Aa", "Bbcde", "abn", "defg", "X", "eq"]

for n in sorted(names, key=len, reverse=True):
    print(n)
