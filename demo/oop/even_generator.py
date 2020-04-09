def even_numbers(start, end):
    if start % 2 != 0:
        start += 1  # Make it even

    for n in range(start, end + 1, 2):
        yield n


g = even_numbers(10,14)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

g = even_numbers(11, 20)
print(type(g))
for n in g:
    print(n)