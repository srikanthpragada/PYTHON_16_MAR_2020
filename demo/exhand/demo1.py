

try:
    v = int(input("Enter a number :"))
    if v % 2 == 0:
        print('Even')
    else:
        print('Odd')
except:
    print('Sorry! Invalid Number!')

print('The End')