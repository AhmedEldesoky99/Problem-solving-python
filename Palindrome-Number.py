print('this program check input number is plindrome or not')

number = input('Enter Number = ')

reversed_num = number[::-1]

if(number == reversed_num):
    print('this number is plindrome')
else:
    print('this number is not plindrome')


