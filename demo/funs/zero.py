def zero(n):
    print("Before change :", id(n))
    n = 0
    print("After change :", id(n))


def prepend(lst, value):
    lst.insert(0, value)


# Effectively pass by reference
nums = [1, 2, 3]   # Mutable
prepend(nums, 10)
print(nums)

# Effectively pass by value
a = 100      # Immutable
print("Before call :", id(a))
zero(a)
print("After call :", id(a))
print(a)
