total = 0
count = 0

while True:
    try:
        n = int(input("Enter a number [0 top stop] :"))
        if n == 0:
            break

        total += n
        count += 1
    except ValueError as ex:
        print("Error :", str(ex))

print(f"Sum = {total}, Average  = {total / count}")
