def fun(**details):
    for k, v in details.items():
        print(k, v)


def fun2(*objects, **details):
    pass


fun(a=10, b=20, message="Hi")

fun2(10, 20, 30, a=10, b="Abc")
