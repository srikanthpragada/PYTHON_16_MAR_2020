def common_factors(n1, n2):
    min = n1 if n1 < n2 else n2
    factors = []
    for i in range(2, min // 2 + 1):
        if n1 % i == 0 and n2 % i == 0:
            factors.append(i)

    return factors


print(common_factors(10, 20))
print(common_factors(100, 120))
