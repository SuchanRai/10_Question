# to find the smallest number among 3
a = int(input(':'))
b = int(input(':'))
c = int(input(':'))
if a>b & a>c:
    print(f'{a} is the greatest')
if b>c & b>a:
    print(f'{b} is the greatest')
if c > b & c > a:
    print(f'{c} is the greatest')