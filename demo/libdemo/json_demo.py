import json


class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s


t = Time(10, 20, 30)
js = json.dumps(t.__dict__)    # Dict to JSON
print(js)

# converting JSON to DICT
d = json.loads(js)
print(d)
