def contains_digit(st):
    for c in st:
        if c.isdigit():
            return True

    return False


strs = ["Alkjsda", "lkjsa334", "34", "lkjsalkfjs"]

for s in filter(contains_digit, strs):
    print(s)
