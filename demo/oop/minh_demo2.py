class A:
    def process(self):
        print("A")


class B(A):
    def process(self):
        print("B")


class C(A):  # Multiple inheritance
    def process(self):
        print("C")


class D(B, C):
    pass


print(D.mro())
