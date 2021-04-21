# accepts marks of four sub. amd display totAL marks , percentage , and grade
math = int(input('Enter your marks of math:'))
computer = int(input('Enter your marks of computer:'))
Account = int(input('Enter your marks of Account:'))
English = int(input('Enter your marks of English:'))
total = math + computer + Account + English
percentage = total /400 * 100
if percentage>70:
    print('Distinction')
elif percentage>60:
    print('First division')
elif percentage>40:
    print('second devision')
elif percentage<40 & percentage>0:
    print('fail')
else:
    print('error, please enter correctly')
print(f'total = {total} percentage = {percentage}% ')