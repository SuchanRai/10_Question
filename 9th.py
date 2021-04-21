# to check the leap year
year = int(input('enter the year'))
if (year/4 == 0) & (year/100 != 0):
    print('LEAP YEAR')
else:
    print('leap year')