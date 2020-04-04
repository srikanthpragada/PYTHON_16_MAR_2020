class Time:
    # Special methods
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    @property
    def hour(self):
        return self.h

    @hour.property
    def hour(self, value):
        if value >= 0 and value <= 23:
            self.h = value

    @property
    def total_seconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    def __int__(self):
        return self.total_seconds

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    def __eq__(self, other):
        return self.total_seconds == other.total_seconds

    def __gt__(self, other):
        print("__gt__()")
        return self.total_seconds > other.total_seconds


t1 = Time(11, 20, 30)
t2 = Time(10, 20, 30)

print(t1)  # str(t1)  -->  t1.__str__()
print(t1 == t2)  # t1.__eq__(t2)
print(t1 != t2)  # t1.__eq__(t2)
print(t1 > t2)  # t1.__gt__(t2)
print(t1 < t2)  # t1.__gt__(t2)

print(10 + int(t1))  # t1.__int__()
