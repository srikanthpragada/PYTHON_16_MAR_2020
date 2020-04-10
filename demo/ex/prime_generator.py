def primes(start, end):
    for n in range(start, end + 1):
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                break
        else:
            yield n


def alphas(st):
    for ch in st:
        if ch.isalpha():
            yield ch


for c in alphas("This is 007"):
    print(c)

for n in primes(100, 200):
    print(n)
