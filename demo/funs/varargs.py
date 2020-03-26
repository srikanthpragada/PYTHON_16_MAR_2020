def hello(*names, message="Hello"):
    for n in names:
        print(message, n)


hello("Steve", "Mike")
hello("Larry", "Scott", "Ben", message="Good Bye")
# hello("Steve","Mike")
