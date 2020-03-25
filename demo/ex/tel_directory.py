dir = {}

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    phone = input("Enter phone :")
    # if name is not present add name as key and phone as element in set
    if name not in dir:
        dir[name] = {phone}  # add new entry
    else:
        dir[name].add(phone)   # add phone to existing entry

for name, phones in sorted(dir.items()):
    print(f"{name:10} {','.join(phones)}")

