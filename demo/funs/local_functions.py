g = 100  # Global variable


def fun1():
    a = 10  # Enclosing variable

    def fun2():
        nonlocal a   # Refer to enclosing variable
        a = a + 10
        b = 20
        print(g, a, b)  # Global, Enclosing, Local

    fun2()
    print(a)


fun1()
