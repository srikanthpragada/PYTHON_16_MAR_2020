# Strong number

org_num = num = int(input("Enter number :"))

total = 0
while num > 0:
    digit = num % 10   # Take rightmost digit
    # Calculate factorial for digit
    fact = 1
    for i in range(2,digit + 1):
        fact = fact * i

    total += fact
    num = num // 10    # Remove rightmost digit

if total == org_num:
    print("Strong Number")
else:
    print("Not a Strong Number")
