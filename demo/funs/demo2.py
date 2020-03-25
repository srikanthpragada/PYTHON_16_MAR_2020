def line(length, ch='-'):
    for i in range(1, length + 1):
        print(ch, end='')


line(ch='*', length=15)  # Keyword argument
print("\nHello")
line(20, '.')  # Positional argument
line(length=20)
