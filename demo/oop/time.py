class Time:
    # Special methods
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"


t1 = Time(10, 20, 30)
t2 = Time(10, 20, 30)

print(t1)   # str(t1)  -->  t1.__str__()
print(t1 == t2)
