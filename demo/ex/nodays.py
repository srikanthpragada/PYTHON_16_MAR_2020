# No. of days in the given month

month = int(input("Enter month :"))
if month == 2:
    nodays = 28
elif month in (4, 6, 9, 11):
    nodays = 30
else:
    nodays = 31

print(f"No. of days = {nodays}")
