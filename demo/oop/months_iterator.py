# Iterator
class Months_Iterator:
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def __next__(self):
        if self.pos == len(self.data):
            raise StopIteration
        else:
            v = self.data[self.pos]
            self.pos += 1
            return v

# Iterable class
class Months:
    names = ["Jan", "Feb", "Mar"]

    def __iter__(self):
       return Months_Iterator(self.names)


m = Months()
for v in m:
    print(v)
