def sumDigits( num : str):
    myList = []
    sum = 0

    for digit in num:
        myList.append(int(digit))

    for digit in myList:
        sum = sum + digit
    
    output = str(sum)
    
    if(len(output) > 1):
        sumDigits(output)
    else:
        print(output)



num = input('Enter the Number: ')
sumDigits(num)