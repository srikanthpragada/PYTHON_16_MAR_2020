def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def mathop(op, a, b):
    return op(a, b)


add2 = add

print(add(10, 20))
print(add2(10, 20))

print(mathop(add, 10, 20))
print(mathop(mul, 10, 20))
