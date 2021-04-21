# add the three number digit
value = int(input('enter the three digit number'))
a = value%10
value = int(value/10)
b = value%10
value = int(value/10)
c = value%10
print(f'the sum is {a+b+c}')
