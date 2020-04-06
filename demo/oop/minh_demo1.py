class A:
    pass
    # def process(self):
    #     print("A")


class B:
    def process(self):
        print("B")


class C(A, B):  # Multiple inheritance
    pass
    # def process(self):
    #     print("C")


obj = C()
obj.process()
