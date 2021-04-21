# check whether 5 is inlist of first 5 natural numbers or not.
a = range(1, 6)
for i in a:
    if i == 5:
        print(' Has 5')
        break
else:
    print('No match found')
