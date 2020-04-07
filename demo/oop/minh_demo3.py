class A:
    def process(self):
        print("A")


class B(A):
    def process(self):
        print("B")


class C(B, A):  # Multiple inheritance
    pass


print(C.mro())
