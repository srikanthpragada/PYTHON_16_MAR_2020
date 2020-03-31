def iseven(n):
    return n % 2 == 0


def isodd(n):
    return n % 2 == 1


# testing, run this only when module is invoked as script
if __name__ == '__main__':
    print("Testing functions...")
    print(iseven(11))
    print(isodd(11))

