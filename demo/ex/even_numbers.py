
nums = []

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break
    if num % 2 == 0:
        nums.append(num)


print(nums)